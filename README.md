# Project 2: Extracting Links from Instagram

Extract clickable post URLs from an Instagram profile (e.g. [@0_shufen](https://www.instagram.com/0_shufen/)).

## Task

1. Open the Instagram profile in a browser (with Chrome remote debugging)
2. Scroll the profile to load posts
3. Extract post URLs — links that open each photo when clicked
4. Save the list for viewing

## Setup

```bash
pip install playwright
playwright install chromium
```

## Usage

**Prerequisites:** Chrome must be running with remote debugging, and you must be logged into Instagram.

1. Quit Chrome, then start it with:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
   ```

2. In that Chrome window, open [instagram.com/0_shufen/](https://www.instagram.com/0_shufen/) and log in.

3. Run the script:
   ```bash
   python get_urls.py --use-chrome
   ```

4. The script scrolls for ~5 seconds, collects post URLs, and prints them.

## Collected URLs

Post URLs from [@0_shufen](https://www.instagram.com/0_shufen/) — click any link while logged in to view the photo:

| # | URL |
|---|-----|
| 1 | https://www.instagram.com/p/DP0MnP4EXZh/ |
| 2 | https://www.instagram.com/p/DPeLJJFkS43/ |
| 3 | https://www.instagram.com/p/DPdYaIQEfaV/ |
| 4 | https://www.instagram.com/p/DOcVa_jkqYw/ |
| 5 | https://www.instagram.com/p/DOZwrNekXl7/ |
| 6 | https://www.instagram.com/p/DOYbZolkey5/ |
| 7 | https://www.instagram.com/p/DN1ytCKZDb-/ |
| 8 | https://www.instagram.com/p/DNpY4gex_nA/ |
| 9 | https://www.instagram.com/p/DMmMPT-SY4b/ |
| 10 | https://www.instagram.com/p/DMM7Gd3SKCD/ |
| 11 | https://www.instagram.com/p/DL8-qvhywdq/ |
| 12 | https://www.instagram.com/p/DL2FC44yuoE/ |
| 13 | https://www.instagram.com/p/DLyv9DkyErt/ |
| 14 | https://www.instagram.com/p/DLuOd_5SsOK/ |
| 15 | https://www.instagram.com/p/DLrkXpDyFaa/ |
| 16 | https://www.instagram.com/p/DLnAOOBSDzN/ |
| 17 | https://www.instagram.com/p/DLe5XNyyy-T/ |
| 18 | https://www.instagram.com/p/DLZTHm0y19f/ |
| 19 | https://www.instagram.com/p/DLUhUq7yW-0/ |
| 20 | https://www.instagram.com/p/DLRhHpPSXvj/ |
| 21 | https://www.instagram.com/p/DLQ4BQBSK_1/ |

URLs are also saved to `image_urls.txt`.

## Push to GitHub

To push this project to [GitHub](https://github.com/cherngywh/-Agentic-AI-Coding-Project-2-Extract-Links-of-Images-from-an-Instagram-Account):

```bash
GITHUB_TOKEN=your_token ./push_to_github.sh
```

Or run the commands in **DEBUG_PUSH.md** for step-by-step push instructions (run in your Terminal — automated push from IDE may not work due to network).

Create a token at https://github.com/settings/tokens with `repo` scope.
