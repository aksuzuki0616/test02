import json
import os
import requests
from datetime import date


START_DATE = date(2026, 5, 3)


def main():
    with open("quotes.json", encoding="utf-8") as f:
        quotes = json.load(f)

    days = (date.today() - START_DATE).days
    index = days % len(quotes)
    quote = quotes[index]

    message = f"✨ **今日の一言**\n\n> {quote['text']}\n\n― {quote['author']}"

    if index == len(quotes) - 1:
        message += "\n\n⚠️ 格言リストが最後の1件です。`quotes.json` に格言を追加してください！"

    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    response = requests.post(webhook_url, json={"content": message})
    response.raise_for_status()
    print(f"投稿しました ({index + 1}/{len(quotes)}): {quote['author']}")


if __name__ == "__main__":
    main()
