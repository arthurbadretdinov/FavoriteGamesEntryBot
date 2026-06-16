from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.entry_form import EntryForm

router = Router()


@router.message(EntryForm.nickname)
async def process_nickname(message: Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    await state.set_state(EntryForm.age)
    await message.answer("Сколько тебе лет?")


@router.message(EntryForm.age)
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(EntryForm.microphone)
    await message.answer("Есть ли у тебя микрофон? (да/нет)")


@router.message(EntryForm.microphone)
async def process_microphone(message: Message, state: FSMContext):
    await state.update_data(microphone=message.text)
    await state.set_state(EntryForm.games)
    await message.answer("Какие игры тебе интересны?")


@router.message(EntryForm.games)
async def process_games(message: Message, state: FSMContext):

    await state.update_data(games=message.text)
    data = await state.get_data()
    await message.answer(
        f"Спасибо! Вот твоя анкета:\n\nНикнейм: {data['nickname']}\nВозраст: {data['age']}\nМикрофон: {data['microphone']}\nИнтересующие игры: {data['games']}"
    )

    await state.clear()
