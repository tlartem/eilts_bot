from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

module_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Listening"), KeyboardButton(text="Reading")]],
    resize_keyboard=True
)
