from typing import Any

from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter


from app.config import ADMIN_CHAT_ID
from app.keyboards.moderation import moderation_kb
from app.states.entry_form import EntryForm
from app.keyboards.entry import microphone_kb

router = Router()


@router.message(EntryForm.nickname)
async def process_nickname(message: Message, state: FSMContext) -> None:
    text: str = (message.text or "").strip()

    if not text:
        await message.answer("Поле не может быть пустым")
        return

    if len(text) < 3:
        await message.answer("Никнейм должен быть минимум 3 символа")
        return

    if len(text) > 20:
        await message.answer("Никнейм не может быть длиннее 20 символов")
        return

    allowed: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_."

    if not all(char in allowed for char in text):
        await message.answer(
            "Никнейм может содержать только латинские буквы, цифры, _ и ."
        )
        return

    await state.update_data(nickname=text)
    await state.set_state(EntryForm.age)
    await message.answer("Сколько тебе лет?")


@router.message(EntryForm.age)
async def process_age(message: Message, state: FSMContext) -> None:
    text: str = (message.text or "").strip()

    if not text.isdigit():
        await message.answer("Введите число (например: 18)")
        return

    age: int = int(text)

    if age < 1 or age > 120:
        await message.answer("Возраст должен быть от 1 до 120")
        return

    await state.update_data(age=age)
    await state.set_state(EntryForm.microphone)
    await message.answer(
        "Есть ли у тебя микрофон? (да/нет)", reply_markup=microphone_kb()
    )


@router.callback_query(
    F.data.in_({"mic_yes", "mic_no"}), StateFilter(EntryForm.microphone)
)
async def process_microphone_callback(query: CallbackQuery, state: FSMContext) -> None:
    value: str = "Есть" if query.data == "mic_yes" else "Нет"

    await state.update_data(microphone=value)
    await state.set_state(EntryForm.games)

    if query.message:
        await query.message.answer("Какие игры тебе интересны? (например: CS2, Dota 2)")

    await query.answer()


@router.message(EntryForm.microphone)
async def process_microphone(message: Message, state: FSMContext) -> None:
    text: str = (message.text or "").strip()

    await state.update_data(microphone=text)
    await state.set_state(EntryForm.games)
    await message.answer("Какие игры тебе интересны?")


@router.message(EntryForm.games)
async def process_games(message: Message, state: FSMContext, bot: Bot) -> None:
    text: str = (message.text or "").strip()

    if not text:
        await message.answer("Напиши хотя бы одну игру (например: CS2, Dota 2)")
        return

    if len(text) > 200:
        await message.answer(
            "Напиши игры через запятую (например: CS2, Dota 2, Valorant)"
        )
        return

    await state.update_data(games=text)

    data: dict[str, Any] = await state.get_data()

    text: str = (
        "Новая анкета:\n\n"
        f"Ник: {data['nickname']}\n"
        f"Возраст: {data['age']}\n"
        f"Микрофон: {data['microphone']}\n"
        f"Игры: {data['games']}"
    )

    await message.answer(text)

    await bot.send_message(
        chat_id=ADMIN_CHAT_ID, text=text, reply_markup=moderation_kb()
    )

    await state.clear()
