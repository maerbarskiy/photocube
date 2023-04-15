from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Инициализация клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
button_info = KeyboardButton('/info')
button_help = KeyboardButton('/help')
button_sticker = KeyboardButton('/sticker')
button_fiKb = KeyboardButton('/inline')
kb.add(button_info).insert(button_help).add(button_sticker).insert(button_fiKb)