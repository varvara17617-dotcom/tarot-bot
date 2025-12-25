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
        "🌙 Привет.\n\n"
        "Я — бот «Карта дня Таро».\n\n"
        "Каждое утро в 7:00 я присылаю одну карту — "
        "спокойное послание и направление на день ✨\n\n"
        "Ничего нажимать не нужно.\n"
        "Просто оставайся здесь 🤍"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



