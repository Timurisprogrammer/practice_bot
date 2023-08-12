from aiogram.dispatcher.filters.state import StatesGroup, State


class FontsStates(StatesGroup):
    strikethrough_state = State()
    underlined_state = State()
    italic_state = State()
    bold_state = State()

