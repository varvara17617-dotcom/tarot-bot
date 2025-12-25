# -*- coding: utf-8 -*-
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

import os
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

tarot_cards = [
    {"name": "Шут", "meaning": "Новые начала, спонтанность, доверие к жизни."},
    {"name": "Маг", "meaning": "Сила воли, инициатива, умение влиять на ситуацию."},
    {"name": "Верховная Жрица", "meaning": "Интуиция, скрытые знания, внутренний голос."},
    {"name": "Императрица", "meaning": "Забота, рост, изобилие и творчество."},
    {"name": "Император", "meaning": "Структура, стабильность, контроль и ответственность."}
]

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "✨ Привет!\n"
        "Я бот «Карта дня Таро».\n\n"
        "Напиши /card, чтобы получить свою карту дня 🔮"
    )

@dp.message(Command("card"))
async def card(message: types.Message):
    card = random.choice(tarot_cards)
    text = f"🔮 *Карта дня:* {card['name']}\n\n{card['meaning']}"
    await message.answer(text, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

