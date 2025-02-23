from aiogram.utils.keyboard import InlineKeyboardBuilder

builder = InlineKeyboardBuilder()
builder.button(text="←")
builder.button(text="→")
builder.adjust(1, 1)
