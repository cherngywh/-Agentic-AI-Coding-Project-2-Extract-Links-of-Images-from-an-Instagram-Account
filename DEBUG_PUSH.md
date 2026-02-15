# Debug: Push to GitHub Not Working

The automated push from this environment **cannot reach GitHub** (likely network/sandbox restrictions). Run the steps below **in your own Terminal** to push successfully.

## Step 1: Verify Your Token

Your token needs `repo` scope. Test it:
```bash
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```
If you see your user info → token works. If 401 → token expired or revoked; create a new one at https://github.com/settings/tokens

## Step 2: Push (copy-paste into Terminal)

```bash
cd "/Users/cherngywhlee/Work/Project 2: Extracting Links from Instagram"

TEMP=$(mktemp -d)
cp README.md get_urls.py requirements.txt image_urls.txt "$TEMP/"
mkdir -p "$TEMP/photo"
cd "$TEMP"

git init
git config user.email "you@example.com"
git config user.name "cherngywh"
git add -A
git commit -m "Add Project 2: Extract links from Instagram"
git branch -M main

git push "https://YOUR_TOKEN@github.com/cherngywh/-Agentic-AI-Coding-Project-2-Extract-Links-of-Images-from-an-Instagram-Account.git" main --force
```

## Step 3: If You See Errors

- **"Authentication failed"** → Token expired/revoked. Create new token at https://github.com/settings/tokens with `repo` scope.
- **"Permission denied"** → Token needs `repo` scope. Edit token, enable "repo".
- **"Repository not found"** → Check the repo exists: https://github.com/cherngywh/-Agentic-AI-Coding-Project-2-Extract-Links-of-Images-from-an-Instagram-Account
- **"Updates were rejected"** → Try adding `--force` (already in command above)

## Step 4: Revoke Token After Push

Go to https://github.com/settings/tokens and delete this token (it was shared in chat).
