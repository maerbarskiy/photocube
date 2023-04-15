from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Инициализация Инлайн клавиатуры
ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url='https://vk.com/maerbarskiy')
ib2 = InlineKeyboardButton(text='Button 2',
                           url='https://twitter.com/maerbarskiy')
ikb.add(ib1).add(ib2)
