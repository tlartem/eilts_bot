from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Тест целиком"), KeyboardButton(text="Модуль")]],
    resize_keyboard=True
)
