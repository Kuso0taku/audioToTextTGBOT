from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


btn_help = KeyboardButton('/help')
kb_help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_help.add(btn_help)
