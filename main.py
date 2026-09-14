import os
import random
import subprocess
import requests
import time
import base64
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# INPUT HELPERS
# ─────────────────────────────────────────────

def get_positive_int(prompt, default=20):
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_repo_path(prompt, default="."):
    while True:
        user_input = input(f"{prompt} (default current directory): ")
        if not user_input.strip():
            return default
        if os.path.isdir(user_input):
            return user_input
        else:
            print("Directory does not exist. Please enter a valid path.")

def get_filename(prompt, default="data.txt"):
    user_input = input(f"{prompt} (default {default}): ")
    return user_input.strip() or default

def get_input(prompt, default=""):
    user_input = input(f"{prompt}" + (f" (default: {default})" if default else "") + ": ")
    return user_input.strip() or default

def yes_no(prompt, default="y"):
    ans = input(f"{prompt} [y/n] (default {default}): ").strip().lower()
    if not ans:
        return default == "y"
    return ans in ("y", "yes")

# ─────────────────────────────────────────────
# GIT / LOCAL COMMIT HELPERS
# ─────────────────────────────────────────────

def random_date_in_last_year():
    today = datetime.now()
    start_date = today - timedelta(days=365)
    random_days = random.randint(0, 364)
    random_seconds = random.randint(0, 23 * 3600 + 3599)
    return start_date + timedelta(days=random_days, seconds=random_seconds)

def make_commit(date, repo_path, filename, message="graph-greener!", coauthor=None):
    filepath = os.path.join(repo_path, filename)
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")
    subprocess.run(["git", "add", filename], cwd=repo_path)
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    # Add co-author trailer for Pair Extraordinaire badge
    commit_msg = message
    if coauthor:
        commit_msg += f"\n\nCo-authored-by: {coauthor}"
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_path, env=env)

# ─────────────────────────────────────────────
# GITHUB API HELPERS
# ─────────────────────────────────────────────

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

def get_branch_sha(token, owner, repo, branch):
    r = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/git/ref/heads/{branch}",
        headers=gh_headers(token),
    )
    r.raise_for_status()
    return r.json()["object"]["sha"]

def create_branch(token, owner, repo, new_branch, sha):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/git/refs",
        headers=gh_headers(token),
        json={"ref": f"refs/heads/{new_branch}", "sha": sha},
    )
    r.raise_for_status()
    return r.json()

def update_file_on_branch(token, owner, repo, branch, filepath, message, content_addition, coauthor=None):
    """Append content to a file on a specific branch via the API."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filepath}"
    r = requests.get(url, headers=gh_headers(token), params={"ref": branch})
    if r.status_code == 200:
        file_data = r.json()
        existing_content = base64.b64decode(file_data["content"]).decode("utf-8")
        sha = file_data["sha"]
    else:
        existing_content = ""
        sha = None

    new_content = existing_content + content_addition
    encoded = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")
    # Add co-author trailer for Pair Extraordinaire
    commit_message = message
    if coauthor:
        commit_message += f"\n\nCo-authored-by: {coauthor}"
    payload = {"message": commit_message, "content": encoded, "branch": branch}
    if sha:
        payload["sha"] = sha
    r = requests.put(url, headers=gh_headers(token), json=payload)
    r.raise_for_status()
    return r.json()

def add_collaborator(token, owner, repo, username, permission="push"):
    r = requests.put(
        f"https://api.github.com/repos/{owner}/{repo}/collaborators/{username}",
        headers=gh_headers(token),
        json={"permission": permission},
    )
    return r.status_code in (201, 204)

def accept_collaborator_invite(token):
    r = requests.get("https://api.github.com/user/repository_invitations", headers=gh_headers(token))
    r.raise_for_status()
    accepted = []
    for invite in r.json():
        res = requests.patch(
            f"https://api.github.com/user/repository_invitations/{invite['id']}",
            headers=gh_headers(token),
        )
        if res.status_code == 204:
            accepted.append(invite["id"])
    return accepted

def create_issue(token, owner, repo, title, body=""):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers=gh_headers(token),
        json={"title": title, "body": body},
    )
    r.raise_for_status()
    return r.json()

def close_issue(token, owner, repo, issue_number):
    r = requests.patch(
        f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}",
        headers=gh_headers(token),
        json={"state": "closed"},
    )
    r.raise_for_status()
    return r.json()

def create_pull_request(token, owner, repo, head_branch, base_branch, title, body=""):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/pulls",
        headers=gh_headers(token),
        json={"title": title, "head": head_branch, "base": base_branch, "body": body},
    )
    r.raise_for_status()
    return r.json()

def close_pull_request(token, owner, repo, pull_number):
    r = requests.patch(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}",
        headers=gh_headers(token),
        json={"state": "closed"},
    )
    r.raise_for_status()
    return r.json()

def add_review_to_pr(token, owner, repo, pull_number, body="LGTM", event="APPROVE"):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        headers=gh_headers(token),
        json={"body": body, "event": event},
    )
    r.raise_for_status()
    return r.json()

def add_pr_comment(token, owner, repo, pull_number, body):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments",
        headers=gh_headers(token),
        json={"body": body},
    )
    r.raise_for_status()
    return r.json()

def merge_pull_request(token, owner, repo, pull_number, commit_title="Merge PR"):
    r = requests.put(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        headers=gh_headers(token),
        json={"commit_title": commit_title, "merge_method": "merge"},
    )
    r.raise_for_status()
    return r.json()

def delete_branch(token, owner, repo, branch):
    r = requests.delete(
        f"https://api.github.com/repos/{owner}/{repo}/git/refs/heads/{branch}",
        headers=gh_headers(token),
    )
    return r.status_code in (204, 422)

def star_repo(token, owner, repo):
    r = requests.put(
        f"https://api.github.com/user/starred/{owner}/{repo}",
        headers={**gh_headers(token), "Content-Length": "0"},
    )
    return r.status_code in (204, 304)

def follow_user(token, username):
    r = requests.put(
        f"https://api.github.com/user/following/{username}",
        headers={**gh_headers(token), "Content-Length": "0"},
    )
    return r.status_code in (204, 304)

# ── GraphQL helpers ──────────────────────────

def graphql(token, query, variables=None):
    r = requests.post(
        "https://api.github.com/graphql",
        headers=gh_headers(token),
        json={"query": query, "variables": variables or {}},
    )
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise Exception(data["errors"])
    return data["data"]

def get_discussion_categories(token, owner, repo):
    data = graphql(token, """
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        discussionCategories(first: 10) { nodes { id name } }
      }
    }""", {"owner": owner, "name": repo})
    return data["repository"]["discussionCategories"]["nodes"]

def create_discussion(token, repo_node_id, category_id, title, body):
    data = graphql(token, """
    mutation($repoId: ID!, $categoryId: ID!, $title: String!, $body: String!) {
      createDiscussion(input: {
        repositoryId: $repoId, categoryId: $categoryId, title: $title, body: $body
      }) { discussion { id number url } }
    }""", {"repoId": repo_node_id, "categoryId": category_id, "title": title, "body": body})
    return data["createDiscussion"]["discussion"]

def add_discussion_comment(token, discussion_id, body):
    data = graphql(token, """
    mutation($discussionId: ID!, $body: String!) {
      addDiscussionComment(input: {discussionId: $discussionId, body: $body}) {
        comment { id }
      }
    }""", {"discussionId": discussion_id, "body": body})
    return data["addDiscussionComment"]["comment"]

def mark_discussion_answer(token, comment_id):
    """Mark a discussion comment as the accepted answer — earns Galaxy Brain."""
    data = graphql(token, """
    mutation($commentId: ID!) {
      markDiscussionCommentAsAnswer(input: {id: $commentId}) {
        discussion { id }
      }
    }""", {"commentId": comment_id})
    return data["markDiscussionCommentAsAnswer"]["discussion"]

# ─────────────────────────────────────────────
# FEATURE MODULES
# ─────────────────────────────────────────────

def run_commits(repo_path, filename, num_commits, coauthor=None):
    """
    Local backdated commits. Pass coauthor='Name <email>' to also
    earn Pair Extraordinaire badge once the PR is merged.
    """
    print(f"\n📝 Making {num_commits} backdated commits in: {repo_path}")
    if coauthor:
        print(f"  Co-authoring with: {coauthor} (Pair Extraordinaire progress)")
    for i in range(num_commits):
        commit_date = random_date_in_last_year()
        print(f"  [{i+1}/{num_commits}] Committing at {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        make_commit(commit_date, repo_path, filename, coauthor=coauthor)
    # Fix detached HEAD — checkout main (or master) before pulling/pushing
    print("\n  Checking branch state...")
    branch_check = subprocess.run(
        ["git", "symbolic-ref", "--short", "HEAD"],
        cwd=repo_path, capture_output=True, text=True
    )
    if branch_check.returncode != 0:
        # Detached HEAD — get the default branch name from remote and check it out
        print("  ℹ️  Detached HEAD detected. Checking out main branch...")
        remote_head = subprocess.run(
            ["git", "remote", "show", "origin"],
            cwd=repo_path, capture_output=True, text=True
        )
        default_branch = "main"
        for line in remote_head.stdout.splitlines():
            if "HEAD branch:" in line:
                default_branch = line.split(":")[-1].strip()
                break
        subprocess.run(["git", "checkout", default_branch], cwd=repo_path)

    print("  Pulling remote changes (rebase)...")
    subprocess.run(["git", "pull", "--rebase", "origin",
                    branch_check.stdout.strip() or "main"], cwd=repo_path)
    print("  Pushing commits...")
    result = subprocess.run(["git", "push"], cwd=repo_path)
    if result.returncode == 0:
        print("  ✅ Commits pushed!")
    else:
        print("  ⚠️  Push failed. Trying force push...")
        result2 = subprocess.run(["git", "push", "--force-with-lease"], cwd=repo_path)
        if result2.returncode == 0:
            print("  ✅ Commits pushed (force)!")
        else:
            print("  ❌ Push still failed. Run manually: git checkout main && git push --force-with-lease")


def run_api_commits(token, owner, repo, num_commits, coauthor=None):
    """
    API commits for account 2's graph (no local git needed).
    Optionally co-authors with account 1 for Pair Extraordinaire.
    """
    print(f"\n📝 Making {num_commits} API commits on {owner}/{repo}")
    default_branch = get_default_branch(token, owner, repo)
    for i in range(num_commits):
        commit_date = random_date_in_last_year()
        content = f"\nAPI Commit #{i+1} at {commit_date.isoformat()}\n"
        message = f"graph-greener: update {i+1}"
        try:
            update_file_on_branch(
                token, owner, repo, default_branch,
                "data.txt", message, content, coauthor=coauthor
            )
            print(f"  [{i+1}/{num_commits}] ✓ {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"  [{i+1}/{num_commits}] ⚠️  Failed: {e}")
        time.sleep(0.5)
    print(f"  ✅ API commits done on {owner}/{repo}")


def run_pull_requests(token, owner, repo, num_prs, second_token=None,
                      acc1_email=None, acc2_email=None):
    """
    Badge flow:
      Account 2 opens PRs with co-author trailer → Account 1 reviews+merges

    Badges earned:
      - Account 2: Pull Shark (merged PRs)
      - Account 1: Code Review (reviewed PRs from someone else)
      - Both:      Pair Extraordinaire (co-authored commits in merged PRs)
      - Quickdraw: handled separately via run_quickdraw()
    """
    print(f"\n🔀 Creating {num_prs} Pull Request(s) on {owner}/{repo}")
    default_branch = get_default_branch(token, owner, repo)

    pr_messages = [
        "chore: update contribution log",
        "docs: minor readme improvements",
        "chore: housekeeping update",
        "fix: minor typo correction",
        "chore: sync data file",
        "docs: add contribution notes",
    ]
    review_comments = [
        "LGTM! Great work.", "Looks good to me.", "Nice clean change, approved.",
        "Reviewed and approved.", "All good here!", "Clean diff, merging.",
    ]

    if second_token:
        second_user = get_authenticated_user(second_token)
        second_username = second_user["login"]
        # Build co-author trailers if emails provided
        coauthor_for_acc2 = f"{github_display_name(token)} <{acc1_email}>" if acc1_email else None
        coauthor_for_acc1 = f"{second_username} <{acc2_email}>" if acc2_email else None

        print(f"  Second account: {second_username}")
        print(f"  Adding {second_username} as collaborator on {owner}/{repo}...")
        add_collaborator(token, owner, repo, second_username, permission="push")

        time.sleep(3)
        try:
            accepted = accept_collaborator_invite(second_token)
            if accepted:
                print(f"  ✓ Collaborator invite accepted by {second_username}")
            else:
                print(f"  ℹ️  No pending invite (may already be a collaborator)")
        except Exception as e:
            print(f"  ℹ️  Auto-accept skipped: {e}")
            print(f"  ℹ️  If needed, accept manually at github.com/{second_username} → notifications")

        for i in range(num_prs):
            branch_name = f"auto-pr-{int(time.time())}-{random.randint(1000,9999)}"
            title = random.choice(pr_messages)
            content = f"\nUpdate #{i+1} at {datetime.now().isoformat()}\n"
            print(f"\n  [{i+1}/{num_prs}] Branch: {branch_name}")

            sha = get_branch_sha(token, owner, repo, default_branch)
            create_branch(second_token, owner, repo, branch_name, sha)
            print(f"    ✓ Branch created by {second_username}")

            # Commit with co-author = account 1 (Pair Extraordinaire for both)
            update_file_on_branch(
                second_token, owner, repo, branch_name,
                "data.txt", title, content, coauthor=coauthor_for_acc2
            )
            print(f"    ✓ File updated by {second_username}" +
                  (f" (co-authored by acc1)" if coauthor_for_acc2 else ""))

            pr = create_pull_request(second_token, owner, repo, branch_name, default_branch, title)
            pr_number = pr["number"]
            print(f"    ✓ PR #{pr_number} opened: {pr['html_url']}")

            # Account 1 reviews → Code Review badge for account 1
            time.sleep(2)
            try:
                add_review_to_pr(token, owner, repo, pr_number,
                                 body=random.choice(review_comments), event="APPROVE")
                print(f"    ✓ Reviewed by {owner}")
            except Exception as e:
                print(f"    ⚠️  Review failed: {e}")

            # Account 1 merges → Pull Shark for account 2
            time.sleep(1)
            try:
                merge_pull_request(token, owner, repo, pr_number, commit_title=title)
                print(f"    ✓ PR #{pr_number} merged")
            except Exception as e:
                print(f"    ⚠️  Merge failed: {e}")

            delete_branch(token, owner, repo, branch_name)
            print(f"    ✓ Branch deleted")
            time.sleep(1)

    else:
        # Single account — still earns Pull Shark
        print("  ℹ️  Single account mode — earning Pull Shark only")
        for i in range(num_prs):
            branch_name = f"auto-pr-{int(time.time())}-{random.randint(1000,9999)}"
            title = random.choice(pr_messages)
            content = f"\nUpdate #{i+1} at {datetime.now().isoformat()}\n"
            print(f"\n  [{i+1}/{num_prs}] Branch: {branch_name}")

            sha = get_branch_sha(token, owner, repo, default_branch)
            create_branch(token, owner, repo, branch_name, sha)
            update_file_on_branch(token, owner, repo, branch_name, "data.txt", title, content)
            pr = create_pull_request(token, owner, repo, branch_name, default_branch, title)
            pr_number = pr["number"]
            print(f"    ✓ PR #{pr_number} opened: {pr['html_url']}")
            time.sleep(1)
            try:
                merge_pull_request(token, owner, repo, pr_number, commit_title=title)
                print(f"    ✓ PR #{pr_number} merged")
            except Exception as e:
                print(f"    ⚠️  Merge failed: {e}")
            delete_branch(token, owner, repo, branch_name)
            time.sleep(1)

    print(f"\n  ✅ Pull Requests done!")
    print(f"  → https://github.com/{owner}?tab=achievements")


def github_display_name(token):
    """Return 'Name <email>' string for the token's account, for co-author trailers."""
    user = get_authenticated_user(token)
    name = user.get("name") or user["login"]
    # GitHub noreply email format
    email = f"{user['id']}+{user['login']}@users.noreply.github.com"
    return f"{name} <{email}>"


def run_quickdraw(token, owner, repo, count=5):
    """
    Quickdraw badge: open an issue or PR then close it within 5 minutes.
    We open an issue and immediately close it — well within the window.
    """
    print(f"\n⚡ Quickdraw: Opening and immediately closing {count} issue(s) on {owner}/{repo}")
    titles = [
        "chore: temp tracking issue",
        "fix: placeholder issue",
        "docs: temp note",
        "chore: cleanup tracker",
        "fix: minor flag",
    ]
    for i in range(count):
        title = random.choice(titles) + f" #{random.randint(100,999)}"
        try:
            issue = create_issue(token, owner, repo, title, body="Auto-generated. Closing immediately.")
            issue_number = issue["number"]
            print(f"  [{i+1}/{count}] Issue #{issue_number} opened")
            time.sleep(1)  # tiny delay, still well under 5 minutes
            close_issue(token, owner, repo, issue_number)
            print(f"  [{i+1}/{count}] ✓ Issue #{issue_number} closed (Quickdraw progress)")
        except Exception as e:
            print(f"  [{i+1}/{count}] ⚠️  Failed: {e}")
        time.sleep(0.5)
    print(f"  ✅ Quickdraw done!")


def run_starstruck(token, owner, repo, second_token=None, extra_tokens=None):
    """
    Starstruck badge: repo needs to be starred by other accounts.
    Account 2 (and any extra tokens) star account 1's repo.
    Thresholds: 16 / 128 / 512 / 4096 stars for Default/Bronze/Silver/Gold
    """
    print(f"\n⭐ Starstruck: Having other accounts star {owner}/{repo}")
    all_tokens = []
    if second_token:
        all_tokens.append(second_token)
    if extra_tokens:
        all_tokens.extend(extra_tokens)

    if not all_tokens:
        print("  ℹ️  No other account tokens provided — can't auto-star your own repo.")
        print(f"  ℹ️  Share your repo and ask others to star: https://github.com/{owner}/{repo}")
        return

    for i, t in enumerate(all_tokens):
        try:
            u = get_authenticated_user(t)
            ok = star_repo(t, owner, repo)
            print(f"  ✓ {u['login']} starred {owner}/{repo}")
        except Exception as e:
            print(f"  ⚠️  Token {i+1} failed: {e}")
    print(f"  ✅ Starstruck stars added!")


def run_stars(token, repos_to_star, default_owner=""):
    """Star a list of repos from account 1."""
    print(f"\n⭐ Starring {len(repos_to_star)} repo(s)...")
    for repo_full in repos_to_star:
        try:
            parts = repo_full.strip().split("/")
            if len(parts) == 1 and default_owner:
                parts = [default_owner, parts[0]]
            if len(parts) != 2:
                print(f"  ⚠️  Invalid format (use owner/repo): {repo_full}")
                continue
            ok = star_repo(token, parts[0], parts[1])
            print(f"  {'✓' if ok else '⚠️'} Starred {parts[0]}/{parts[1]}")
        except Exception as e:
            print(f"  ⚠️  Failed: {e}")


def run_follows(token, users_to_follow):
    print(f"\n👥 Following {len(users_to_follow)} user(s)...")
    for username in users_to_follow:
        try:
            ok = follow_user(token, username.strip())
            print(f"  {'✓' if ok else '⚠️'} Followed {username}")
        except Exception as e:
            print(f"  ⚠️  Failed: {e}")


def run_discussions(token, owner, repo, num_discussions, second_token=None, acc1_username=None):
    """
    Galaxy Brain badge:
      - Account 1 creates a discussion in a Q&A category
      - Account 2 posts an answer
      - Account 1 marks account 2's answer as accepted
        → Account 2 earns Galaxy Brain

    OR single account:
      - Account 1 creates discussion and self-answers
      - Cannot self-mark as accepted (GitHub blocks this)
      - Still builds discussion activity
    """
    print(f"\n💬 Creating {num_discussions} Discussion(s) on {owner}/{repo}")

    try:
        categories = get_discussion_categories(token, owner, repo)
    except Exception as e:
        print(f"  ⚠️  Could not fetch categories: {e}")
        print(f"  ℹ️  Enable Discussions at: https://github.com/{owner}/{repo}/settings")
        return

    if not categories:
        print(f"  ⚠️  No discussion categories found.")
        print(f"  ℹ️  Enable Discussions at: https://github.com/{owner}/{repo}/settings")
        return

    print(f"  Categories: {[c['name'] for c in categories]}")
    # Q&A category is required to mark accepted answers (Galaxy Brain)
    qa_category = next((c for c in categories if "q" in c["name"].lower() and "a" in c["name"].lower()), None)
    general_category = next((c for c in categories if "general" in c["name"].lower()), None)
    category = qa_category or general_category or categories[0]
    print(f"  Using: {category['name']}" + (" ✓ (Q&A supports accepted answers)" if qa_category else " ⚠️  (use Q&A category for Galaxy Brain)"))

    repo_node_id = get_repo_info(token, owner, repo)["node_id"]

    if second_token:
        second_user = get_authenticated_user(second_token)
        second_username = second_user["login"]
        print(f"  Account 2 ({second_username}) will answer → account 1 marks accepted")

    questions = [
        "What's the best way to structure a Python project?",
        "How do you handle secrets in GitHub Actions?",
        "Tips for writing good commit messages?",
        "What's your preferred git branching strategy?",
        "How do you keep dependencies up to date?",
        "Best practices for code review etiquette?",
        "How do you document APIs effectively?",
        "What's the best way to handle database migrations?",
    ]
    answers_pool = [
        "I follow the src layout with a dedicated tests/ folder. Keeps things clean.",
        "GitHub Secrets + OIDC for cloud providers. Never hardcode credentials.",
        "Conventional commits (feat/fix/chore) + imperative mood. Short subject line.",
        "Trunk-based development for small teams, GitFlow for larger release cycles.",
        "Dependabot or Renovate bot — automated PRs keep you on top of updates.",
        "Be specific, not personal. Review the code, not the author.",
        "OpenAPI/Swagger for REST, inline docstrings for internal APIs.",
        "Always include a rollback migration alongside the forward migration.",
    ]

    for i in range(num_discussions):
        title = random.choice(questions) + f" ({i+1})"
        body = "Looking for community insights on this topic."
        answer_body = random.choice(answers_pool)

        print(f"\n  [{i+1}/{num_discussions}] \"{title}\"")
        try:
            discussion = create_discussion(token, repo_node_id, category["id"], title, body)
            print(f"    ✓ Discussion created: {discussion['url']}")
            time.sleep(1)

            if second_token:
                # Account 1 posts the answer
                comment = add_discussion_comment(token, discussion["id"], answer_body)
                comment_id = comment["id"]
                print(f"    ✓ Answer posted by {acc1_username or owner} (account 1)")
                time.sleep(1)
                # Account 2 marks account 1's answer as accepted
                # → Account 1 earns Galaxy Brain badge
                try:
                    mark_discussion_answer(second_token, comment_id)
                    print(f"    ✓ Accepted by {second_username} (account 2) → Galaxy Brain for {acc1_username or owner} 🧠")
                except Exception as e:
                    print(f"    ⚠️  Could not mark answer (needs Q&A category): {e}")
            else:
                # No second account — account 1 answers its own discussion
                # GitHub does NOT allow self-accepting answers, so no Galaxy Brain
                comment = add_discussion_comment(token, discussion["id"], answer_body)
                print(f"    ✓ Answer posted by {acc1_username or owner}")
                print(f"    ℹ️  Cannot self-accept — add a second account token for Galaxy Brain")

        except Exception as e:
            print(f"    ⚠️  Failed: {e}")
        time.sleep(1)

    print(f"\n  ✅ Discussions done!")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print("=" * 60)
    print("🌱 graph-greener — GitHub Activity & Badge Booster 🌱")
    print("=" * 60)
    print("Badges: Pull Shark · Code Review · Quickdraw · Pair Extraordinaire · Starstruck · Galaxy Brain\n")

    # ── Account 1 token ──
    token = get_input("Enter your GitHub Personal Access Token (account 1)")
    if not token:
        print("❌ Token is required. Exiting.")
        return
    try:
        user = get_authenticated_user(token)
        github_username = user["login"]
        print(f"  ✓ Account 1: {github_username}\n")
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return

    # ── Account 2 token (optional but recommended) ──
    second_token = get_input("Enter SECOND account token (optional, press Enter to skip)")
    second_username = None
    if second_token:
        try:
            second_user = get_authenticated_user(second_token)
            second_username = second_user["login"]
            print(f"  ✓ Account 2: {second_username}")
        except Exception as e:
            print(f"  ⚠️  Second token invalid: {e}")
            second_token = None

    # ── Which features ──
    print("\n" + "─" * 60)
    print("Select features (press Enter = yes):")
    do_commits        = yes_no("1. Backdated commits for account 1 (green graph + Pair Extraordinaire)")
    do_prs            = yes_no("2. Pull Requests: acc2 opens → acc1 reviews+merges (Pull Shark + Code Review)")
    do_quickdraw      = yes_no("3. Quickdraw: open+close issues instantly")
    do_pair           = yes_no("4. Pair Extraordinaire: API commits with co-author trailer")
    do_starstruck     = yes_no("5. Starstruck: acc2 stars acc1's repo")
    do_second_commits = yes_no("6. API commits for account 2 (green their graph)")
    do_stars          = yes_no("7. Star other repos (optional)")
    do_follows        = yes_no("8. Follow users (optional)")
    do_discussions    = yes_no("9. Galaxy Brain: discussions with accepted answers")
    print("─" * 60)

    # ── Repo details ──
    if any([do_prs, do_quickdraw, do_pair, do_starstruck, do_discussions]):
        repo_owner = get_input("GitHub repo owner", github_username)
        repo_name  = get_input("GitHub repo name on account 1 (must exist)")
    else:
        repo_owner = github_username
        repo_name  = ""

    second_repo_name = ""
    if (do_second_commits or do_pair) and second_token:
        second_repo_name = get_input(f"Repo name on account 2 ({second_username}) for API commits (must exist)")

    print()

    # ── 1. Local backdated commits ──
    if do_commits:
        repo_path = get_repo_path("Path to local git repo")
        filename  = get_filename("Filename to modify", "data.txt")
        num_commits = get_positive_int("Number of commits", 20)
        # Co-author with account 2 for Pair Extraordinaire
        coauthor = None
        if second_username:
            coauthor = f"{second_username} <{second_user['id']}+{second_username}@users.noreply.github.com>"
        run_commits(repo_path, filename, num_commits, coauthor=coauthor)

    # ── 2. Pull Requests ──
    if do_prs and repo_name:
        num_prs = get_positive_int("Number of PRs to create", 5)
        run_pull_requests(token, repo_owner, repo_name, num_prs, second_token)

    # ── 3. Quickdraw ──
    if do_quickdraw and repo_name:
        count = get_positive_int("Number of issues to open+close (Quickdraw)", 5)
        run_quickdraw(token, repo_owner, repo_name, count)

    # ── 4. Pair Extraordinaire via API commits ──
    if do_pair and second_token and repo_name:
        print(f"\n🤝 Pair Extraordinaire: API commits with co-author on {repo_owner}/{repo_name}")
        num_pair = get_positive_int("Number of co-authored API commits", 10)
        acc2_coauthor = f"{second_username} <{second_user['id']}+{second_username}@users.noreply.github.com>"
        # Make commits on acc1 repo co-authored by acc2
        update_branch = get_default_branch(token, repo_owner, repo_name)
        for i in range(num_pair):
            content = f"\nPair commit #{i+1} at {datetime.now().isoformat()}\n"
            try:
                update_file_on_branch(
                    token, repo_owner, repo_name, update_branch,
                    "data.txt", f"chore: pair commit {i+1}", content,
                    coauthor=acc2_coauthor
                )
                print(f"  [{i+1}/{num_pair}] ✓ Co-authored commit pushed")
            except Exception as e:
                print(f"  [{i+1}/{num_pair}] ⚠️  {e}")
            time.sleep(0.5)
        print(f"  ✅ Pair Extraordinaire commits done!")

    # ── 5. Starstruck ──
    if do_starstruck and repo_name:
        run_starstruck(token, repo_owner, repo_name, second_token=second_token)

    # ── 6. API commits for account 2 ──
    if do_second_commits and second_token and second_repo_name:
        num_api = get_positive_int(f"Number of API commits for {second_username}", 20)
        acc1_coauthor = f"{github_username} <{user['id']}+{github_username}@users.noreply.github.com>"
        run_api_commits(second_token, second_username, second_repo_name, num_api, coauthor=acc1_coauthor)

    # ── 7. Stars ──
    if do_stars:
        print("\nEnter repos to star (owner/repo), empty line to finish:")
        repos = []
        while True:
            line = input("  repo: ").strip()
            if not line:
                break
            repos.append(line)
        if repos:
            run_stars(token, repos, default_owner=github_username)

    # ── 8. Follows ──
    if do_follows:
        print("\nEnter usernames to follow, empty line to finish:")
        users = []
        while True:
            line = input("  username: ").strip()
            if not line:
                break
            users.append(line)
        if users:
            run_follows(token, users)

    # ── 9. Discussions (Galaxy Brain) ──
    if do_discussions and repo_name:
        print(f"\n  ℹ️  Enable Discussions + Q&A category at:")
        print(f"  https://github.com/{repo_owner}/{repo_name}/settings")
        num_disc = get_positive_int("Number of discussions to create", 3)
        run_discussions(token, repo_owner, repo_name, num_disc, second_token=second_token, acc1_username=github_username)

    print("\n" + "=" * 60)
    print("🎉 All done!")
    print(f"   Account 1 badges: https://github.com/{github_username}?tab=achievements")
    if second_username:
        print(f"   Account 2 badges: https://github.com/{second_username}?tab=achievements")
    print("=" * 60)


if __name__ == "__main__":
    main()
