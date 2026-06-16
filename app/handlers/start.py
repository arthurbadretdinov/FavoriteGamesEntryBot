from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.entry_form import EntryForm

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.set_state(EntryForm.nickname)
    await message.answer(
        "Привет!\n"
        "Это бот для вступления в беседу Favorite Games.\n\n"
        "Я задам тебе несколько вопросов — это займёт 1–2 минуты.\n\n"
        "Напиши свой игровой ник"
    )
