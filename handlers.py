from aiogram import types, Dispatcher
import commands


def registered_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands='start')
    dp.register_message_handler(commands.input_url, commands='url')
