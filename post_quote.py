import json
import os
import hashlib
import requests
from datetime import datetime


def main():
    with open("quotes.json", encoding="utf-8") as f:
        quotes = json.load(f)

    date_str = datetime.now().strftime("%Y-%m-%d")
    index = int(hashlib.md5(date_str.encode()).hexdigest(), 16) % len(quotes)
    quote = quotes[index]

    message = f"✨ **今日の一言**\n\n> {quote['text']}\n\n― {quote['author']}"

    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    response = requests.post(webhook_url, json={"content": message})
    response.raise_for_status()
    print(f"投稿しました: {quote['author']}")


if __name__ == "__main__":
    main()
