from config import dp, bot
from aiogram import types
# from Keyboards import menu_buttons
from pytube import YouTube
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import Text

@dp.message_handler(commands='start')
async def start_bot(message: types.Message, inLine_keyboard=None):
    await message.reply(f'Привет, {message.from_user.first_name}!')
    await message.answer("Вставьте ссылку чтобы скачать видео. Используйте /url")


@dp.message_handler(commands='url')
async def input_url(message: types.Message):
    msg = message.text.split()
    if len(msg) > 2:
        res = msg[2]
    else:
        res = '720p'
    yt = YouTube(msg[1])
    print(yt.watch_url)
    path = yt.title
    yt.streams.filter(resolution=res).first().download('')
    print('Загрузка завершена')
