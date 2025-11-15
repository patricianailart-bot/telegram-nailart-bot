import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка
if not BOT_TOKEN:
    raise ValueError("ERROR: BOT_TOKEN is missing in environment variables!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот успешно работает! 👋")

# Все сообщения
@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    import asyncio
    asyncio.run(main())
