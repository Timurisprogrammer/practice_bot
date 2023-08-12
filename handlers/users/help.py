from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp

@dp.message_handler(Command('help'))
async def help_cmd(message:types.Message):
    await message.answer('to use this bot press start to summon the keyboard  \n'
                         'after that you will see a bunch of font titles press on one you like\n'
                         'after that type in something and bot will answer you with text with font you pick ')