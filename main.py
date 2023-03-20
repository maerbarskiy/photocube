import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import API_TOKEN, HELP_COMMAND
# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Инициализация bot и dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Инициализация клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
button_info = KeyboardButton('/info')
button_help = KeyboardButton('/help')
button_sticker = KeyboardButton('/sticker')
kb.add(button_info).add(button_help).add(button_sticker)


# Сообщение в терминале после запуска бота
async def on_startup(_):
    print('Бот был успешно запущен, красава бро!')


# Сообщение после команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('<a href="https://t.me/maer_news/64">Здарова</a>, '
                         'я буду за тобой повторять', parse_mode='HTML',
                         reply_markup=kb)
    await message.delete()


# Сообщение после команды /info
@dp.message_handler(commands=['info'])
async def show_info(message: types.Message):
    await message.answer("Напишите команду /help для получения списка команд")
    await message.delete()


# Вывод списка команд, командой /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['sticker'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEIJ5BkEpN8UgcAARc4YnpUiG-ol0xNv0IAAkQBAAIrTg0TFZs6V0d0kI0vBA")
    await message.delete()


@dp.message_handler()
async def echo_upper(message: types.Message):
    await message.answer(text=message.text.upper())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    