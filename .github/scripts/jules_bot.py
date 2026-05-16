#!/usr/bin/env python3
"""
Jules Bot – uses Google Jules (Gemini) API to interpret @jules prompts
and perform GitHub actions (create/update files, open PRs, comment).
"""

import os
import json
import re
from github import Github, GithubException
import google.generativeai as genai

# ------------------------------------------------------------
# 1. Load environment
# ------------------------------------------------------------
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
JULES_API_KEY = os.environ["JULES_API_KEY"]
REPO_NAME = os.environ["REPO_FULL_NAME"]
COMMENT_BODY = os.environ["COMMENT_BODY"]
COMMENT_USER = os.environ["COMMENT_USER"]

# Determine if it's an issue or a PR
issue_number = os.environ.get("ISSUE_NUMBER")
pr_number = os.environ.get("PR_NUMBER")
if issue_number:
    comment_target = ("issue", int(issue_number))
else:
    comment_target = ("pr", int(pr_number))

# Extract the prompt after "@jules"
match = re.search(r"@jules\s+(.+)", COMMENT_BODY, re.IGNORECASE | re.DOTALL)
if not match:
    print("No @jules prompt found – exiting")
    exit(0)
prompt = match.group(1).strip()

# ------------------------------------------------------------
# 2. Initialise clients
# ------------------------------------------------------------
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
genai.configure(api_key=JULES_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')   # or your Google Jules model

def post_comment(message: str):
    if comment_target[0] == "issue":
        repo.get_issue(comment_target[1]).create_comment(message)
    else:
        repo.get_pull(comment_target[1]).create_issue_comment(message)

# ------------------------------------------------------------
# 3. Get repository context (file tree + previews)
# ------------------------------------------------------------
def get_repo_context():
    contents = repo.get_contents("")
    tree = []
    for item in contents:
        entry = {"path": item.path, "type": item.type}
        if item.type == "file" and item.path.endswith((".py", ".md", ".txt", ".json", ".yaml", ".toml")):
            try:
                content = item.decoded_content.decode("utf-8", errors="ignore")[:2000]
                entry["preview"] = content
            except:
                pass
        tree.append(entry)
    return tree

context = get_repo_context()

# ------------------------------------------------------------
# 4. Ask Google Jules (Gemini) to generate actions in JSON
# ------------------------------------------------------------
system_prompt = """You are Jules, an AI assistant that helps with coding tasks.
You can read and write files, create commits, and post comments.
Given the user's prompt and the current repository context, output a JSON object
with the actions to perform.

Allowed actions:
- "comment": string – a message to post as a comment (optional)
- "files": list of file operations:
    - "path": relative file path
    - "operation": "create" | "update" | "delete"
    - "content": for create/update, the new content (string)
- "branch_name": optional name for a new branch (default: "jules-{timestamp}")
- "commit_message": commit message (default: "Jules bot update")

Example for "write a python hello world script":
{
  "comment": "I created hello.py with a hello world program.",
  "branch_name": "jules-hello",
  "commit_message": "Add hello world script",
  "files": [
    {"path": "hello.py", "operation": "create", "content": "print('Hello, World!')"}
  ]
}

For "write all code in this repo with python": generate a complete Python project structure based on the repo's existing files and purpose.
"""

user_prompt = f"""Repository context (top-level files/folders):
{json.dumps(context, indent=2)}

User prompt: {prompt}

Produce the JSON actions. If you cannot fulfill the request exactly, explain why in a comment and suggest alternatives.
Output ONLY valid JSON, no other text.
"""

response = model.generate_content(
    system_prompt + "\n\n" + user_prompt,
    generation_config={"response_mime_type": "application/json"}
)

try:
    actions = json.loads(response.text)
except Exception as e:
    post_comment(f"❌ Jules failed to parse the AI response: {e}\n```\n{response.text}\n```")
    exit(1)

# ------------------------------------------------------------
# 5. Execute the actions (same as before)
# ------------------------------------------------------------
branch_name = actions.get("branch_name", f"jules-{os.urandom(4).hex()}")
commit_msg = actions.get("commit_message", "Jules bot update")
files_to_change = actions.get("files", [])
reply_comment = actions.get("comment", "")

if not files_to_change:
    if reply_comment:
        post_comment(reply_comment)
    else:
        post_comment("✅ Jules received your prompt, but no actions were generated.")
    exit(0)

# Create a new branch from default branch
default_branch = repo.default_branch
base_sha = repo.get_branch(default_branch).commit.sha
try:
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_sha)
except GithubException as e:
    post_comment(f"⚠️ Could not create branch `{branch_name}`: {e.data.get('message', e)}")
    exit(1)

# Apply file operations
for file_op in files_to_change:
    path = file_op["path"]
    op = file_op["operation"]
    content = file_op.get("content", "")
    try:
        if op == "delete":
            file_obj = repo.get_contents(path, ref=branch_name)
            repo.delete_file(path, f"Delete {path}", file_obj.sha, branch=branch_name)
        elif op in ("create", "update"):
            try:
                existing = repo.get_contents(path, ref=branch_name)
                repo.update_file(path, commit_msg, content, existing.sha, branch=branch_name)
            except GithubException:
                repo.create_file(path, commit_msg, content, branch=branch_name)
    except Exception as e:
        post_comment(f"❌ Failed to {op} `{path}`: {e}")
        exit(1)

# Create Pull Request
pr_title = f"Jules: {prompt[:60]}..."
pr_body = f"🤖 **Jules** responded to @{COMMENT_USER}:\n\n> {prompt}\n\n"
if reply_comment:
    pr_body += f"{reply_comment}\n\n"
pr_body += f"Branch: `{branch_name}`\n\nPlease review and merge."

try:
    pr = repo.create_pull(
        title=pr_title,
        body=pr_body,
        head=branch_name,
        base=default_branch
    )
    final_msg = f"✅ Jules created pull request #{pr.number} with the requested changes.\n{pr.html_url}"
    if reply_comment:
        final_msg += f"\n\n**Comment from Jules:** {reply_comment}"
    post_comment(final_msg)
except Exception as e:
    post_comment(f"❌ Jules created the branch but failed to open a PR: {e}")
