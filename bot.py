from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from os import remove

from config import TOKEN
from script import STT
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('🇺🇸: Hello!\n🇷🇺: Привет!', reply_markup=kb.kb_help)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('🇺🇸 Send me audio and I\'ll send u text!\n🇷🇺 Отправь мне аудио, а я тебе отправлю текст!')

@dp.message_handler(content_types=['document', 'audio', 'voice'])
async def process_STT_command(msg: types.Message):
    name = 'output.wav'
    await bot.send_message(msg.from_user.id, '🇺🇸 Recognizing...\n🇷🇺 Обработка...')
    if msg.content_type in ['audio']:
        await msg.audio.download(name)
    elif msg.content_type in ['voice']:
        await msg.voice.download(name)
    elif msg.content_type in ['document']:
        await msg.document.download(name)
    message = STT().LargeAudioFile(name)
    if not message:
        message = '🇺🇸 I can\'t recognize this, try again!\n🇷🇺 Я не могу это распознать, попробуйте снова!'
    await msg.reply(message)
    remove(name)

@dp.message_handler(content_types=['any'])
async def echo_command(message: types.Message):
    await bot.send_message(message.from_user.id, '🇺🇸 Send me audio!\n🇷🇺 Отправьте мне аудио!')

if __name__ == '__main__':
    executor.start_polling(dp)
