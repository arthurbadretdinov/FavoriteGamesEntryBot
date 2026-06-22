from aiogram.fsm.state import StatesGroup, State


class RejectState(StatesGroup):
    waiting_reason = State()
