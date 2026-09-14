"""
Daily automation script — runs 1 of each activity.
Designed to be called by GitHub Actions or cron.
Reads tokens from environment variables:
  GITHUB_TOKEN_1  — account 1 (main account)
  GITHUB_TOKEN_2  — account 2 (second account)
  GITHUB_REPO     — repo name on account 1 (e.g. "prev")
"""

import os
import random
import requests
import time
import base64
from datetime import datetime

# ── reuse helpers from main.py ──────────────────

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

def update_file_on_branch(token, owner, repo, branch, filepath, message, content, coauthor=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filepath}"
    r = requests.get(url, headers=gh_headers(token), params={"ref": branch})
    if r.status_code == 200:
        existing = base64.b64decode(r.json()["content"]).decode("utf-8")
        sha = r.json()["sha"]
    else:
        existing = ""
        sha = None
    new_content = existing + content
    encoded = base64.b64encode(new_content.encode()).decode()
    commit_message = message
    if coauthor:
        commit_message += f"\n\nCo-authored-by: {coauthor}"
    payload = {"message": commit_message, "content": encoded, "branch": branch}
    if sha:
        payload["sha"] = sha
    r = requests.put(url, headers=gh_headers(token), json=payload)
    r.raise_for_status()
    return r.json()

def create_pull_request(token, owner, repo, head, base, title):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/pulls",
        headers=gh_headers(token),
        json={"title": title, "head": head, "base": base, "body": "Daily automated PR."},
    )
    r.raise_for_status()
    return r.json()

def add_review_to_pr(token, owner, repo, pull_number, body, event="APPROVE"):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        headers=gh_headers(token),
        json={"body": body, "event": event},
    )
    r.raise_for_status()
    return r.json()

def merge_pull_request(token, owner, repo, pull_number, title):
    r = requests.put(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        headers=gh_headers(token),
        json={"commit_title": title, "merge_method": "merge"},
    )
    r.raise_for_status()
    return r.json()

def delete_branch(token, owner, repo, branch):
    requests.delete(
        f"https://api.github.com/repos/{owner}/{repo}/git/refs/heads/{branch}",
        headers=gh_headers(token),
    )

def create_issue(token, owner, repo, title):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers=gh_headers(token),
        json={"title": title, "body": "Daily automated issue."},
    )
    r.raise_for_status()
    return r.json()

def close_issue(token, owner, repo, number):
    r = requests.patch(
        f"https://api.github.com/repos/{owner}/{repo}/issues/{number}",
        headers=gh_headers(token),
        json={"state": "closed"},
    )
    r.raise_for_status()

def accept_collaborator_invite(token):
    r = requests.get("https://api.github.com/user/repository_invitations", headers=gh_headers(token))
    if r.status_code != 200:
        return
    for invite in r.json():
        requests.patch(
            f"https://api.github.com/user/repository_invitations/{invite['id']}",
            headers=gh_headers(token),
        )

def add_collaborator(token, owner, repo, username):
    requests.put(
        f"https://api.github.com/repos/{owner}/{repo}/collaborators/{username}",
        headers=gh_headers(token),
        json={"permission": "push"},
    )

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
    graphql(token, """
    mutation($commentId: ID!) {
      markDiscussionCommentAsAnswer(input: {id: $commentId}) {
        discussion { id }
      }
    }""", {"commentId": comment_id})

# ── daily activities ────────────────────────────

def daily_commit(token, owner, repo, default_branch, coauthor=None):
    content = f"\nDaily commit at {datetime.now().isoformat()}\n"
    message = f"chore: daily update {datetime.now().strftime('%Y-%m-%d')}"
    update_file_on_branch(token, owner, repo, default_branch, "data.txt", message, content, coauthor=coauthor)
    print("✅ Daily commit done")

def daily_pr(token, owner, repo, default_branch, second_token, second_username):
    branch = f"daily-{datetime.now().strftime('%Y%m%d')}-{random.randint(100,999)}"
    title = f"chore: daily update {datetime.now().strftime('%Y-%m-%d')}"
    content = f"\nPR update at {datetime.now().isoformat()}\n"

    sha = get_branch_sha(token, owner, repo, default_branch)
    create_branch(second_token, owner, repo, branch, sha)
    update_file_on_branch(second_token, owner, repo, branch, "data.txt", title, content)
    pr = create_pull_request(second_token, owner, repo, branch, default_branch, title)
    pr_number = pr["number"]
    print(f"✅ PR #{pr_number} opened by {second_username}")

    time.sleep(3)
    add_review_to_pr(token, owner, repo, pr_number, "LGTM!", event="APPROVE")
    print(f"✅ PR #{pr_number} reviewed by account 1")

    time.sleep(2)
    merge_pull_request(token, owner, repo, pr_number, title)
    print(f"✅ PR #{pr_number} merged")

    delete_branch(token, owner, repo, branch)

def daily_issue(token, owner, repo):
    titles = [
        "chore: daily tracking issue",
        "fix: daily placeholder",
        "docs: daily note",
        "chore: daily cleanup",
    ]
    title = random.choice(titles) + f" {datetime.now().strftime('%Y-%m-%d')}"
    issue = create_issue(token, owner, repo, title)
    time.sleep(2)
    close_issue(token, owner, repo, issue["number"])
    print(f"✅ Issue #{issue['number']} opened+closed (Quickdraw)")

def daily_discussion(token, owner, repo, second_token):
    repo_info = get_repo_info(token, owner, repo)
    repo_node_id = repo_info["node_id"]
    categories = get_discussion_categories(token, owner, repo)
    qa = next((c for c in categories if "q" in c["name"].lower() and "a" in c["name"].lower()), None)
    if not qa:
        print("⚠️  No Q&A category found — skipping discussion")
        return

    questions = [
        "Best way to structure a monorepo?",
        "How do you handle API versioning?",
        "Tips for writing clean Python code?",
        "How do you manage tech debt effectively?",
        "What's your approach to testing microservices?",
        "How do you document internal tools?",
        "Best practices for Git branching?",
        "How do you handle breaking changes in APIs?",
        "What's your CI/CD pipeline look like?",
        "How do you onboard new developers?",
        "Tips for effective code reviews?",
        "How do you prioritize bug fixes vs features?",
        "Best way to handle async errors in Python?",
        "How do you keep documentation up to date?",
    ]
    answers = [
        "Keep each package self-contained with its own tests and build scripts.",
        "Use versioned URL paths (/v1/, /v2/) and deprecate old versions with clear timelines.",
        "Follow PEP8, use type hints, keep functions small and single-purpose.",
        "Schedule regular refactor sprints and track debt in issues.",
        "Contract testing with Pact, integration tests against real instances in CI.",
        "Readme-driven development — write the docs before the code.",
        "Trunk-based for small teams, GitFlow for scheduled releases.",
        "Semantic versioning + changelogs + migration guides for every breaking change.",
        "GitHub Actions: lint → test → build → deploy on every merge to main.",
        "Pair programming first week, structured code walkthrough, assigned mentor.",
        "Be specific about what to change and why. Approve fast, block rarely.",
        "User-facing bugs first, then security, then performance, then features.",
        "Use asyncio with proper exception handlers and structured logging.",
        "Treat docs as code — PR reviews required for doc changes too.",
    ]

    title = random.choice(questions) + f" [{datetime.now().strftime('%Y-%m-%d')}]"
    body = "Looking for community thoughts on this."
    answer_body = random.choice(answers)

    discussion = create_discussion(token, repo_node_id, qa["id"], title, body)
    print(f"✅ Discussion created: {discussion['url']}")

    time.sleep(2)
    comment = add_discussion_comment(token, discussion["id"], answer_body)
    print(f"✅ Answer posted by account 1")

    time.sleep(2)
    mark_discussion_answer(second_token, comment["id"])
    print(f"✅ Answer accepted by account 2 → Galaxy Brain for account 1 🧠")

# ── main ────────────────────────────────────────

def main():
    token1  = os.environ.get("GITHUB_TOKEN_1")
    token2  = os.environ.get("GITHUB_TOKEN_2")
    repo    = os.environ.get("GITHUB_REPO", "prev")

    if not token1:
        raise SystemExit("❌ GITHUB_TOKEN_1 env var not set")
    if not token2:
        raise SystemExit("❌ GITHUB_TOKEN_2 env var not set")

    user1 = get_authenticated_user(token1)
    user2 = get_authenticated_user(token2)
    owner = user1["login"]
    second_username = user2["login"]

    print(f"Account 1: {owner}")
    print(f"Account 2: {second_username}")
    print(f"Repo: {owner}/{repo}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    default_branch = get_default_branch(token1, owner, repo)

    # Ensure account 2 is a collaborator
    add_collaborator(token1, owner, repo, second_username)
    time.sleep(3)
    try:
        accept_collaborator_invite(token2)
    except Exception:
        pass

    # Co-author string for Pair Extraordinaire
    coauthor2 = f"{second_username} <{user2['id']}+{second_username}@users.noreply.github.com>"

    # 1. Daily commit (account 1, co-authored by account 2)
    print("── 1. Daily commit ──")
    try:
        daily_commit(token1, owner, repo, default_branch, coauthor=coauthor2)
    except Exception as e:
        print(f"⚠️  Commit failed: {e}")

    time.sleep(2)

    # 2. Daily PR (account 2 opens, account 1 reviews+merges)
    print("── 2. Daily PR ──")
    try:
        daily_pr(token1, owner, repo, default_branch, token2, second_username)
    except Exception as e:
        print(f"⚠️  PR failed: {e}")

    time.sleep(2)

    # 3. Daily issue (open+close for Quickdraw)
    print("── 3. Daily issue (Quickdraw) ──")
    try:
        daily_issue(token1, owner, repo)
    except Exception as e:
        print(f"⚠️  Issue failed: {e}")

    time.sleep(2)

    # 4. Daily discussion (account 1 answers, account 2 accepts → Galaxy Brain)
    print("── 4. Daily discussion (Galaxy Brain) ──")
    try:
        daily_discussion(token1, owner, repo, token2)
    except Exception as e:
        print(f"⚠️  Discussion failed: {e}")

    print(f"\n🎉 Daily run complete!")
    print(f"   https://github.com/{owner}?tab=achievements")

if __name__ == "__main__":
    main()
