# -*- coding: utf-8 -*-

import random
import os
import requests
from cards import tarot_cards

BOT_TOKEN = os.getenv("BOT_TOKEN")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    })

def main():
    # выбираем карту
    card = random.choice(tarot_cards)

    message = (
        f"🌙 *Карта дня*\n\n"
        f"*{card['name']}*\n\n"
        f"{card['meaning']}\n\n"
        "_Прими это как знак, не как приговор._"
    )

    # читаем всех подписанных пользователей
    if not os.path.exists("users.txt"):
        return

    with open("users.txt", "r", encoding="utf-8") as f:
        chat_ids = f.read().splitlines()

    for chat_id in chat_ids:
        send_message(chat_id.strip(), message)

if __name__ == "__main__":
    main()

