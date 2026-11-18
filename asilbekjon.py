import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

# BotFather'dan olgan tokenni shu yerga yozing
TOKEN ="9011715394:AAEDVT1z_kFPw0401fKoZMpUXKaviBvS6Z"

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i uchun javob
@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Botimizga xush kelibsiz.")

# Foydalanuvchi "salom" deb yozsa ishlaydigan qism (katta-kichik harflarga eʼtibor bermaydi)
@dp.message(F.text.lower() == "salom")
async def send_welcome(message: Message):
    await message.answer("Salom! Sizga qanday yordam bera olaman?")

# Botni ishga tushirish funksiyasi
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")
