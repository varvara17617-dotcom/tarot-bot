# -*- coding: utf-8 -*-
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

import os
TOKEN = os.getenv("BOT_TOKEN")

from cards import TAROT_CARDS

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "✨ Привет!\n"
        "Я бот «Карта дня Таро».\n\n"
        "Напиши /card, чтобы получить свою карту дня 🔮"
    )

@dp.message(Command("card"))
async def card(message: types.Message):
    card = random.choice(TAROT_CARDS)

    text = (
        f"🔮 *Карта дня: {card['name']}*\n\n"
        f"{card['meaning']}\n\n"
        "_Прими это как знак, не как приговор._"
    )

    await message.answer(text, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


