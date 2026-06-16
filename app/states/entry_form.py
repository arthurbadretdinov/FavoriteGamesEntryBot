from aiogram.fsm.state import State, StatesGroup


class EntryForm(StatesGroup):
    nickname = State()
    age = State()
    microphone = State()
    games = State()
