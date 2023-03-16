import logging

from aiogram import Bot, Dispatcher, executor, types

from token_api import API_TOKEN
# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Инициализация bot и dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def sed_welcome(message: types.Message):
    await message.reply("Здарова, я буду за тобой повторять")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
