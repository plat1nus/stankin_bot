"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

API_TOKEN = '5855113265:AAHR19MCB9qnlKQRnpRImGpvwxO4WrzOi2o'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Химия", "Русский", "Биология"]
    keyboard.add(*buttons)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Химия"))
async def with_puree(message: types.Message):
    await message.reply("Задания по химии")
    
@dp.message_handler(Text(equals="Русский"))
async def with_puree(message: types.Message):
    await message.reply("Задания по русскому")

@dp.message_handler(Text(equals="Биология"))
async def with_puree(message: types.Message):
    await message.reply("Задания по биологии")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)