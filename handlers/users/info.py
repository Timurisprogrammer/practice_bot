from aiogram import types
from aiogram.dispatcher.filters.builtin import types, Command
from loader import dp
text = 'Hello! what this bot can do? this  bot can change fonts'
@dp.message_handler(Command('info'))
async def info_cmd(message:types.Message):
    await message.answer(text)