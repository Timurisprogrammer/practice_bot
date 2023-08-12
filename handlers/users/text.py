from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


from loader import dp
from states.font_states import FontsStates


@dp.message_handler(state=FontsStates.bold_state)
async def Bold_changer(message:types.Message,state:FSMContext):
    await message.answer(f'<b>{message.text}</b>')
    await state.reset_state()
@dp.message_handler(state=FontsStates.italic_state)
async def italic_changer(message:types.Message,state:FSMContext):
    await message.answer(f'<i>{message.text}</i>')
    await state.reset_state()
    
@dp.message_handler(state=FontsStates.strikethrough_state)
async def underlined_changer(message:types.Message,state:FSMContext):
    await message.answer(f'<s>{message.text}</s>')
    await state.reset_state()

@dp.message_handler(state=FontsStates.underlined_state)
async def underlined_changer(message:types.Message,state:FSMContext):
    await message.answer(f'<u>{message.text}</u>')
    await state.reset_state()


@dp.message_handler(Text(equals='<b>bold</b>'))
async def bold_font(message:types.Message):
    await message.answer(f'<b> BOLD - type in here </b>')
    await FontsStates.bold_state.set()



@dp.message_handler(Text(equals='<i>italic</i>'))
async def italic_font(message:types.Message):
    await message.answer(f'<i>italic - type in here</i>')
    await FontsStates.italic_state.set()

@dp.message_handler(Text(equals='<u>underlined</u>'))
async def underlined_font(message:types.Message):
    await message.answer(f'<u>underlined - type in here</u>')
    await FontsStates.underlined_state.set()

@dp.message_handler(Text(equals='<s>strikethrough</s>'))
async def strikethrough_font(message:types.Message):
    await message.answer(f'<s>strikethrough - type in here</s>')
    await FontsStates.strikethrough_state.set()