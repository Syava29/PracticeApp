import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '1361809459:AAGEsQwtWAXHFqmlzQJJDVBPPhBBU9_GtXI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

button_1 = KeyboardButton('РЦД 👋')
button_2 = KeyboardButton('Я здесь')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1).add(button_2)

inline_btn_1 = InlineKeyboardButton('Группа ВК', url="https://vk.com/tarasenko_pn")
inline_btn_2 = InlineKeyboardButton('Контакты команды', url="https://vk.com/tarasenko_pn")
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply('Привет 👋\nвот перечень команд:\n /info --- Основная информация\n ', reply_markup=greet_kb)

@dp.message_handler(commands=['info'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Основная информация о РЦД", reply_markup=inline_kb1)



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)