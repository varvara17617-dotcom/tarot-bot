# -*- coding: utf-8 -*-

import random
import os
import requests
from cards import tarot_cards

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS")  # через запятую

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    })

def main():
    card = random.choice(tarot_cards)

    message = (
        f"🌙 *Карта дня*\n\n"
        f"*{card['name']}*\n\n"
        f"{card['meaning']}"
    )

    for chat_id in CHAT_IDS.split(","):
        send_message(chat_id.strip(), message)

if __name__ == "__main__":
    main()
