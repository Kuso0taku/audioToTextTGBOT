from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType

from config import TOKEN
from script import STT


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('🇺🇸: Hello!\n🇷🇺: Привет!')

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('🇺🇸: Send me audio and I\'ll send u text!\n🇷🇺: Отправь мне аудио, а я тебе отправлю текст!')


if __name__ == '__main__':
    executor.start_polling(dp)
