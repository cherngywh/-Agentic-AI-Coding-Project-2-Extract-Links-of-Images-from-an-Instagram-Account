#!/bin/bash
# Push Project 2 to: https://github.com/cherngywh/-Agentic-AI-Coding-Project-2-Extract-Links-of-Images-from-an-Instagram-Account
# Usage: GITHUB_TOKEN=your_token ./push_to_github.sh
# Or: ./push_to_github.sh   (will prompt for token)

set -e
cd "$(dirname "$0")"

TOKEN="${GITHUB_TOKEN:-}"
if [ -z "$TOKEN" ]; then
  echo "Enter your GitHub Personal Access Token:"
  read -s TOKEN
  echo ""
fi
if [ -z "$TOKEN" ]; then
  echo "Error: Token required. Run: GITHUB_TOKEN=xxx ./push_to_github.sh"
  exit 1
fi

echo "Creating clean repo with Project 2 content..."
TEMP=$(mktemp -d)
cp README.md get_urls.py requirements.txt image_urls.txt "$TEMP/" 2>/dev/null || true
mkdir -p "$TEMP/photo"
cd "$TEMP"

git init
git config user.email "cherngywh@users.noreply.github.com"
git config user.name "cherngywh"
git add -A
git commit -m "Add Project 2: Extract links from Instagram"

echo "Pushing to GitHub..."
git branch -M main
git push "https://${TOKEN}@github.com/cherngywh/-Agentic-AI-Coding-Project-2-Extract-Links-of-Images-from-an-Instagram-Account.git" main --force

rm -rf "$TEMP"
echo "Done! https://github.com/cherngywh/-Agentic-AI-Coding-Project-2-Extract-Links-of-Images-from-an-Instagram-Account"
