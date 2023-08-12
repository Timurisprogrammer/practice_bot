from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True, keyboard=[
    [KeyboardButton(text='<b>bold</b>')],
    [KeyboardButton(text='<i>italic</i>')],
    [KeyboardButton(text='<u>underlined</u>')],
    [KeyboardButton(text='<s>strikethrough</s>')],
    

])