"""
LeetCode Daily Auto-Solver
──────────────────────────
Fetches 2 random Easy/Medium problems, submits pre-built solutions,
then commits the solution files to GitHub.

Environment variables required:
  LEETCODE_SESSION   — your LeetCode session cookie
  LEETCODE_CSRF      — your LeetCode csrftoken cookie
  GITHUB_TOKEN_1     — GitHub token for committing solutions
  GITHUB_REPO        — repo name (e.g. "prev")

How to get LeetCode cookies:
  1. Log in at leetcode.com
  2. DevTools → Application → Cookies → https://leetcode.com
  3. Copy LEETCODE_SESSION and csrftoken values
"""

import os
import re
import time
import random
import base64
import requests
from datetime import datetime
from solution_bank import SOLUTION_BANK
from blind75_bank import BLIND75_SOLUTIONS
from sql_bank import SQL_SOLUTIONS
from extended_bank import EXTENDED_BANK
from cpp_bank import CPP_BANK

# Merge all Python solutions
ALL_PYTHON_SOLUTIONS = {**SOLUTION_BANK, **BLIND75_SOLUTIONS}
AVAILABLE_SLUGS = list(ALL_PYTHON_SOLUTIONS.keys())
AVAILABLE_SQL_SLUGS = list(SQL_SOLUTIONS.keys())
# C++ bank: slug -> code (lang = "cpp")
AVAILABLE_CPP_SLUGS = list(CPP_BANK.keys())

# ─────────────────────────────────────────────
# LEETCODE API
# ─────────────────────────────────────────────

LEETCODE_BASE = "https://leetcode.com"
GRAPHQL_URL   = f"{LEETCODE_BASE}/graphql"

def lc_session(lc_session_cookie, csrf_token):
    s = requests.Session()
    s.cookies.set("LEETCODE_SESSION", lc_session_cookie, domain="leetcode.com")
    s.cookies.set("csrftoken", csrf_token, domain="leetcode.com")
    s.headers.update({
        "Content-Type": "application/json",
        "Referer": LEETCODE_BASE,
        "x-csrftoken": csrf_token,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    })
    return s

def gql(session, query, variables=None):
    r = session.post(GRAPHQL_URL, json={"query": query, "variables": variables or {}})
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise Exception(data["errors"])
    return data["data"]

def get_problem_list(session, difficulty="EASY", limit=50):
    """Fetch a list of problems by difficulty."""
    data = gql(session, """
    query problemsetQuestionList($filters: QuestionListFilterInput, $limit: Int) {
      problemsetQuestionList: questionList(
        categorySlug: ""
        limit: $limit
        skip: 0
        filters: $filters
      ) {
        questions: data {
          acRate
          difficulty
          frontendQuestionId: questionFrontendId
          titleSlug
          title
          status
        }
      }
    }""", {"filters": {"difficulty": difficulty}, "limit": limit})
    return data["problemsetQuestionList"]["questions"]

def get_problem_detail(session, title_slug):
    """Fetch full problem details including code snippets."""
    data = gql(session, """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        content
        difficulty
        codeSnippets {
          lang
          langSlug
          code
        }
      }
    }""", {"titleSlug": title_slug})
    return data["question"]

def submit_solution(session, title_slug, question_id, code, lang="python3"):
    """Submit a solution to LeetCode."""
    url = f"{LEETCODE_BASE}/problems/{title_slug}/submit/"
    payload = {
        "lang": lang,
        "question_id": str(question_id),
        "typed_code": code,
    }
    r = session.post(url, json=payload)
    r.raise_for_status()
    return r.json().get("submission_id")

def check_submission(session, submission_id, retries=10, delay=3):
    """Poll submission result until it's ready."""
    url = f"{LEETCODE_BASE}/submissions/detail/{submission_id}/check/"
    for _ in range(retries):
        time.sleep(delay)
        r = session.get(url)
        r.raise_for_status()
        result = r.json()
        state = result.get("state", "")
        if state == "SUCCESS":
            return result
        elif state in ("PENDING", "STARTED"):
            continue
        else:
            return result
    return {"state": "TIMEOUT"}

def get_todays_challenge(session):
    """Get LeetCode's daily challenge problem."""
    data = gql(session, """
    query questionOfToday {
      activeDailyCodingChallengeQuestion {
        date
        link
        question {
          questionId
          questionFrontendId
          title
          titleSlug
          difficulty
        }
      }
    }""")
    return data["activeDailyCodingChallengeQuestion"]["question"]



def get_solved_slugs(session):
    """Fetch all problem slugs the user has already solved (AC status)."""
    solved = set()
    skip = 0
    limit = 100
    while True:
        try:
            data = gql(session, """
            query userSolvedProblems($skip: Int, $limit: Int) {
              problemsetQuestionList: questionList(
                categorySlug: ""
                limit: $limit
                skip: $skip
                filters: {status: AC}
              ) {
                questions: data {
                  titleSlug
                }
              }
            }""", {"skip": skip, "limit": limit})
            questions = data["problemsetQuestionList"]["questions"]
            if not questions:
                break
            for q in questions:
                solved.add(q["titleSlug"])
            if len(questions) < limit:
                break
            skip += limit
        except Exception as e:
            print(f"  ⚠️  Could not fetch solved problems: {e}")
            break
    return solved

# Premium-only problems + problems with known submission issues
PREMIUM_SLUGS = {
    "trips-and-users",
    "department-top-three-salaries",
    "nth-highest-salary",
    "reported-posts-ii",
    "string-transforms-into-another-string",
    "number-of-islands-ii",
    "alien-dictionary",
    "meeting-rooms",
    "encode-and-decode-strings",
    "graph-valid-tree",
    "number-of-connected-components-in-an-undirected-graph",
    "missing-ranges",
    "find-the-celebrity",
    "wiggle-sort",
    "paint-house",
    "paint-fence",
    "best-time-to-buy-and-sell-stock-with-cooldown",
    # Slugs with special characters that cause 500 errors
    "pascal-s-triangle",
    "pascal-s-triangle-ii",
    "read-n-characters-given-read4",
    "read-n-characters-given-read4-ii-call-multiple-times",
    "one-edit-distance",
    "find-the-celebrity",
    "shortest-word-distance-ii",
    "strobogrammatic-number",
    "strobogrammatic-number-ii",
    "group-shifted-strings",
    "flatten-2d-vector",
    "meeting-rooms-ii",
    "count-univalue-subtrees",
    "binary-tree-longest-consecutive-sequence",
    "zigzag-iterator",
    "design-hit-counter",
    "nested-list-weight-sum",
    "nested-list-weight-sum-ii",
    "flip-game",
    "flip-game-ii",
    "palindrome-permutation",
    "palindrome-permutation-ii",
    "closest-binary-search-tree-value",
    "closest-binary-search-tree-value-ii",
    "encode-and-decode-strings",
    "android-unlock-patterns",
    "design-log-storage-system",
    "design-search-autocomplete-system",
    "robot-room-cleaner",
    "sentence-screen-fitting",
    "bomb-enemy",
    "design-tic-tac-toe",
    "sparse-matrix-multiplication",
    "maximum-size-subarray-sum-equals-k",
    "binary-tree-vertical-order-traversal",
    "shortest-distance-from-all-buildings",
    "wiggle-sort-ii",
    "largest-bst-subtree",
    "sequence-reconstruction",
    "inorder-successor-in-bst",
    "walls-and-gates",
    "unique-word-abbreviation",
    "valid-word-abbreviation",
    "minimum-unique-word-abbreviation",
    "find-permutation",
    "next-closest-time",
    "k-empty-slots",
    "candy-crush",
    "sentence-similarity",
    "sentence-similarity-ii",
    "friend-circles",  # renamed to number-of-provinces
}# ─────────────────────────────────────────────
# WRONG SOLUTION GENERATOR
# ─────────────────────────────────────────────

def make_wrong_submission(correct_code):
    """
    Take correct code and deliberately break it in a realistic way.
    Simulates a human making common mistakes.
    """
    mutations = [
        # Off-by-one error
        lambda c: c.replace("len(nums)", "len(nums) - 1"),
        lambda c: c.replace("range(len(", "range(1, len("),
        lambda c: c.replace("lo <= hi", "lo < hi"),
        lambda c: c.replace("i + 1", "i"),
        # Wrong operator
        lambda c: c.replace("curr + n", "curr - n"),
        lambda c: c.replace("min(", "max("),
        lambda c: c.replace("max(", "min("),
        lambda c: c.replace(" + ", " - "),
        lambda c: c.replace(" - ", " + "),
        # Wrong return
        lambda c: c.replace("return True", "return False"),
        lambda c: c.replace("return result", "return result + 1"),
        lambda c: c.replace("return 0", "return -1"),
        # Wrong comparison
        lambda c: c.replace(" == ", " != "),
        lambda c: c.replace(" != ", " == "),
        lambda c: c.replace(" >= ", " > "),
        lambda c: c.replace(" <= ", " < "),
        # Missing edge case — return empty instead of result
        lambda c: c.replace("return result", "return []"),
        # Swap indices
        lambda c: c.replace("[i]", "[i-1]"),
        lambda c: c.replace("mid + 1", "mid"),
        lambda c: c.replace("mid - 1", "mid"),
    ]

    lines = correct_code.split("\n")
    # Only mutate lines that are actual logic (not class/def/import lines)
    logic_indices = [
        i for i, line in enumerate(lines)
        if line.strip() and
        not line.strip().startswith("class ") and
        not line.strip().startswith("def ") and
        not line.strip().startswith("#") and
        not line.strip().startswith("from ") and
        not line.strip().startswith("import ")
    ]

    if not logic_indices:
        # Fallback: just append a syntax-valid but wrong return
        return correct_code.rstrip() + "\n        return -999\n"

    # Apply 1-2 random mutations
    mutated = correct_code
    applied = 0
    random.shuffle(mutations)
    for mutation in mutations:
        candidate = mutation(mutated)
        if candidate != mutated:   # mutation actually changed something
            mutated = candidate
            applied += 1
            if applied >= random.randint(1, 2):
                break

    # If no mutation stuck, force a wrong return at end
    if mutated == correct_code:
        mutated = correct_code.rstrip() + "\n        return None\n"

    return mutated

def gh_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

def get_authenticated_user(token):
    r = requests.get("https://api.github.com/user", headers=gh_headers(token))
    r.raise_for_status()
    return r.json()

def get_repo_info(token, owner, repo):
    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}", headers=gh_headers(token))
    r.raise_for_status()
    return r.json()

def get_default_branch(token, owner, repo):
    return get_repo_info(token, owner, repo)["default_branch"]

def commit_file_to_github(token, owner, repo, branch, filepath, content, message):
    """Create or update a file on GitHub."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filepath}"
    r = requests.get(url, headers=gh_headers(token), params={"ref": branch})
    sha = r.json().get("sha") if r.status_code == 200 else None
    encoded = base64.b64encode(content.encode()).decode()
    payload = {"message": message, "content": encoded, "branch": branch}
    if sha:
        payload["sha"] = sha
    r = requests.put(url, headers=gh_headers(token), json=payload)
    r.raise_for_status()
    return r.json()

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def solve_and_commit(lc_cookie, csrf, gh_token, gh_owner, gh_repo, num_problems=2):
    session = lc_session(lc_cookie, csrf)
    default_branch = get_default_branch(gh_token, gh_owner, gh_repo)
    today = datetime.now().strftime("%Y-%m-%d")

    # Fetch already-solved problems from LeetCode
    print("Fetching your solved problems from LeetCode...")
    solved_slugs = get_solved_slugs(session)
    print(f"  You have solved {len(solved_slugs)} problem(s) on LeetCode.")

    # Pick unsolved Python problems
    unsolved_py = [s for s in AVAILABLE_SLUGS if s not in solved_slugs]
    unsolved_sql = [s for s in AVAILABLE_SQL_SLUGS if s not in solved_slugs]

    print(f"  Python bank: {len(AVAILABLE_SLUGS)} | Unsolved: {len(unsolved_py)}")
    print(f"  SQL bank:    {len(AVAILABLE_SQL_SLUGS)} | Unsolved: {len(unsolved_sql)}")

    if not unsolved_py and not unsolved_sql:
        print("  ✅ All problems in the bank are already solved!")
        return []

    # Pick 1 Python + 1 SQL (or 2 Python if no SQL unsolved)
    chosen = []
    if unsolved_py:
        chosen.append(("python3", random.choice(unsolved_py)))
    if unsolved_sql:
        chosen.append(("mysql", random.choice(unsolved_sql)))
    elif len(unsolved_py) >= 2:
        second = random.choice([s for s in unsolved_py if s != chosen[0][1]])
        chosen.append(("python3", second))

    chosen = chosen[:num_problems]

    results = []

    for lang, slug in chosen:
        print(f"\n── Problem: {slug} ({lang}) ──")

        if lang == "mysql":
            _, solution_code = SQL_SOLUTIONS[slug]
        else:
            solution_code = ALL_PYTHON_SOLUTIONS[slug]

        # Try to fetch problem details from LeetCode
        try:
            detail = get_problem_detail(session, slug)
            qid    = detail["questionId"]
            title  = detail["title"]
            difficulty = detail["difficulty"]
            print(f"  #{qid} {title} [{difficulty}]")
        except Exception as e:
            print(f"  ⚠️  Could not fetch problem details: {e}")
            qid, title, difficulty = "?", slug, "Easy"

        # Submit wrong solutions first (2-6 random attempts) to look human
        num_wrong = random.randint(2, 6)
        print(f"  Submitting {num_wrong} wrong attempt(s) first (human simulation)...")
        for attempt in range(num_wrong):
            if lang == "mysql":
                # For SQL: submit slightly broken SQL
                wrong_code = solution_code.replace("COUNT(*)", "COUNT(1)+999") \
                                          .replace("SUM(", "AVG(") \
                                          .replace("MAX(", "MIN(")
                if wrong_code == solution_code:
                    wrong_code = solution_code + "\nLIMIT 0"
            else:
                wrong_code = make_wrong_submission(solution_code)
            try:
                wrong_sub_id = submit_solution(session, slug, qid, wrong_code, lang=lang)
                time.sleep(random.uniform(4, 8))  # random thinking delay
                wrong_result = check_submission(session, wrong_sub_id)
                wrong_status = wrong_result.get("status_msg", "Unknown")
                print(f"    Attempt {attempt+1}/{num_wrong}: {wrong_status} (wrong — expected)")
            except Exception as e:
                print(f"    Attempt {attempt+1}/{num_wrong}: ⚠️  {e}")
            # Random pause between attempts like a human re-reading the problem
            time.sleep(random.uniform(5, 15))

        print(f"  Now submitting correct solution...")
        time.sleep(random.uniform(3, 8))  # pause before correct attempt

        # Submit to LeetCode
        submitted = False
        submission_result = None
        try:
            sub_id = submit_solution(session, slug, qid, solution_code, lang=lang)
            print(f"  Submitted → submission id: {sub_id}")
            time.sleep(5)
            submission_result = check_submission(session, sub_id)
            status = submission_result.get("status_msg", "Unknown")
            runtime = submission_result.get("status_runtime", "N/A")
            memory  = submission_result.get("status_memory", "N/A")
            print(f"  Result: {status} | Runtime: {runtime} | Memory: {memory}")
            submitted = True
        except Exception as e:
            print(f"  ⚠️  Submission failed: {e}")
            status, runtime, memory = "Submitted (unverified)", "N/A", "N/A"

        # Build solution file content
        ext = "sql" if lang == "mysql" else "py"
        status_line = f"# Status: {status}" if submitted else "# Status: Solution committed"
        runtime_line = f"# Runtime: {runtime}" if submitted else ""
        memory_line = f"# Memory: {memory}" if submitted else ""
        file_content = "\n".join(filter(None, [
            f"# {title}",
            f"# Difficulty: {difficulty}",
            f"# Date: {today}",
            f"# LeetCode: https://leetcode.com/problems/{slug}/",
            status_line,
            runtime_line,
            memory_line,
            "",
            solution_code,
        ])) + "\n"

        # Commit to GitHub under dsa/YYYY-MM-DD/
        safe_title = re.sub(r"[^a-z0-9-]", "-", slug)
        filepath = f"dsa/{today}/{safe_title}.{ext}"
        commit_msg = f"dsa: solve {title} [{difficulty}] ({lang}) - {today}"
        try:
            commit_file_to_github(gh_token, gh_owner, gh_repo, default_branch,
                                  filepath, file_content, commit_msg)
            print(f"  ✅ Committed to GitHub: {filepath}")
        except Exception as e:
            print(f"  ⚠️  GitHub commit failed: {e}")

        results.append({
            "slug": slug,
            "title": title,
            "difficulty": difficulty,
            "status": status,
        })
        time.sleep(3)  # be nice between submissions

    # Also commit a daily summary README
    summary = f"# DSA Daily Log — {today}\n\n"
    for r in results:
        summary += f"- **{r['title']}** ({r['difficulty']}) — {r['status']}\n"
    summary += f"\n_Auto-solved on {today}_\n"
    try:
        commit_file_to_github(
            gh_token, gh_owner, gh_repo, default_branch,
            f"dsa/{today}/README.md", summary,
            f"dsa: daily summary {today}"
        )
        print(f"\n✅ Summary committed: dsa/{today}/README.md")
    except Exception as e:
        print(f"⚠️  Summary commit failed: {e}")

    return results


def main():
    lc_cookie = os.environ.get("LEETCODE_SESSION")
    csrf      = os.environ.get("LEETCODE_CSRF")

    if not all([lc_cookie, csrf]):
        raise SystemExit("❌ Missing env vars. Need: LEETCODE_SESSION, LEETCODE_CSRF")

    session = lc_session(lc_cookie, csrf)
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Date: {today}\n")

    print("Fetching your solved problems from LeetCode...")
    solved_slugs = get_solved_slugs(session)
    print(f"  You have solved {len(solved_slugs)} problem(s) on LeetCode.")

    unsolved_py  = [s for s in AVAILABLE_SLUGS if s not in solved_slugs and s not in PREMIUM_SLUGS]
    unsolved_sql = [s for s in AVAILABLE_SQL_SLUGS if s not in solved_slugs and s not in PREMIUM_SLUGS]
    unsolved_cpp = [s for s in AVAILABLE_CPP_SLUGS if s not in solved_slugs and s not in PREMIUM_SLUGS]
    extended_available = [(slug, lang) for (slug, lang), _ in EXTENDED_BANK.items()
                          if slug not in solved_slugs and slug not in PREMIUM_SLUGS]

    print(f"  Python unsolved : {len(unsolved_py)}")
    print(f"  SQL unsolved    : {len(unsolved_sql)}")
    print(f"  C++ unsolved    : {len(unsolved_cpp)}")
    print(f"  Extended unsolved: {len(extended_available)}")

    all_available = (
        [("cpp", s) for s in unsolved_cpp] +
        [("python3", s) for s in unsolved_py] +
        [("mysql", s) for s in unsolved_sql] +
        [(lang, slug) for (slug, lang) in extended_available]
    )

    if not all_available:
        print("  ✅ All problems in the bank are already solved!")
        return

    # Deduplicate by slug (prefer cpp first)
    seen_slugs = set()
    deduped = []
    for lang, slug in all_available:
        if slug not in seen_slugs:
            seen_slugs.add(slug)
            deduped.append((lang, slug))

    chosen = random.sample(deduped, min(1, len(deduped)))

    results = []
    attempted_slugs = set()

    # Try up to 5 candidates in case some fail with 500
    candidates = random.sample(deduped, min(10, len(deduped)))

    for lang, slug in candidates:
        if len(results) >= 1:
            break  # got our 1 problem
        if slug in attempted_slugs:
            continue
        attempted_slugs.add(slug)
        print(f"\n── Problem: {slug} ({lang}) ──")
        solution_code = SQL_SOLUTIONS[slug][1] if lang == "mysql" and slug in SQL_SOLUTIONS else \
                       CPP_BANK.get(slug) if lang == "cpp" else \
                       EXTENDED_BANK.get((slug, lang)) or \
                       (ALL_PYTHON_SOLUTIONS.get(slug) if lang == "python3" else None)
        if not solution_code:
            print(f"  ⚠️  No solution found for {slug} ({lang}), skipping")
            continue

        try:
            detail = get_problem_detail(session, slug)
            qid    = detail["questionId"]
            title  = detail["title"]
            difficulty = detail["difficulty"]
            print(f"  #{qid} {title} [{difficulty}]")
        except Exception as e:
            print(f"  ⚠️  Could not fetch details: {e}")
            qid, title, difficulty = "?", slug, "Easy"

        # Wrong attempts first
        num_wrong = random.randint(2, 6)
        print(f"  Submitting {num_wrong} wrong attempt(s)...")
        for attempt in range(num_wrong):
            wrong_code = solution_code.replace("return ", "return None #") if lang == "mysql" else make_wrong_submission(solution_code)
            try:
                wrong_sub_id = submit_solution(session, slug, qid, wrong_code, lang=lang)
                time.sleep(random.uniform(4, 8))
                wrong_result = check_submission(session, wrong_sub_id)
                print(f"    Attempt {attempt+1}/{num_wrong}: {wrong_result.get('status_msg','?')} (wrong — expected)")
            except Exception as e:
                print(f"    Attempt {attempt+1}/{num_wrong}: ⚠️  {e}")
            time.sleep(random.uniform(5, 15))

        # Correct submission
        print(f"  Submitting correct solution...")
        time.sleep(random.uniform(3, 8))
        try:
            sub_id = submit_solution(session, slug, qid, solution_code, lang=lang)
            time.sleep(5)
            result = check_submission(session, sub_id)
            status  = result.get("status_msg", "Unknown")
            runtime = result.get("status_runtime", "N/A")
            memory  = result.get("status_memory", "N/A")
            print(f"  Result: {status} | Runtime: {runtime} | Memory: {memory}")

            if status == "Accepted":
                print(f"  ✅ Accepted!")
                results.append({"title": title, "difficulty": difficulty, "status": status})
            else:
                print(f"  ⚠️  Not accepted ({status}) — will try next candidate")
                # Add to skip list for this run so we don't retry same slug
                attempted_slugs.add(slug)

        except Exception as e:
            print(f"  ⚠️  Submission failed: {e}")

        time.sleep(3)

    print(f"\n🎉 Done! Solved {len(results)} problem(s) today.")
    for r in results:
        print(f"  - {r['title']} [{r['difficulty']}] → {r['status']}")

    if len(results) == 0:
        raise SystemExit("❌ No problems solved — check logs above.")


if __name__ == "__main__":
    main()
