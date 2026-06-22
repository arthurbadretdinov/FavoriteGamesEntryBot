from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.keyboards.invite import invite_kb
from app.states.moderation import RejectState

router = Router()


@router.callback_query(F.data.startswith("approve_user:"))
async def approve(query: CallbackQuery, bot: Bot):
    if not query.data:
        return

    user_id = int(query.data.split(":")[1])

    await bot.send_message(
        user_id,
        "✅ Твоя заявка принята!\nДобро пожаловать в беседу! 👇",
        reply_markup=invite_kb(),
    )

    message = query.message
    if not isinstance(message, Message):
        return

    await message.edit_reply_markup()
    await query.answer()


@router.callback_query(F.data.startswith("reject_user:"))
async def reject(query: CallbackQuery, state: FSMContext):
    if not query.data:
        return

    user_id = int(query.data.split(":")[1])

    await state.update_data(user_id=user_id)

    await state.set_state(RejectState.waiting_reason)

    message = query.message
    if not isinstance(message, Message):
        return

    await message.edit_reply_markup()
    await message.answer("✍️ Напиши причину отказа:")
    await query.answer()


@router.message(RejectState.waiting_reason)
async def reject_finish(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    user_id = data.get("user_id")

    if user_id is None:
        await message.answer("❌ Ошибка: user_id не найден в состоянии")
        await state.clear()
        return

    reason = message.text

    await bot.send_message(user_id, f"❌ Твоя заявка отклонена.\n" f"Причина: {reason}")

    await state.clear()
