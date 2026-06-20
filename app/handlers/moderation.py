from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message

from app.keyboards.invite import invite_kb

router = Router()


@router.callback_query(F.data.startswith("approve_user:"))
async def approve(query: CallbackQuery, bot: Bot):
    if not query.data:
        return

    user_id = int(query.data.split(":")[1])

    await bot.send_message(user_id, "✅ Твоя заявка принята!")
    await bot.send_message(
        user_id,
        "🎉 Твоя заявка принята!\nДобро пожаловать в беседу! 👇",
        reply_markup=invite_kb(),
    )

    message = query.message
    if not isinstance(message, Message):
        return

    await message.edit_reply_markup()
    await query.answer()


@router.callback_query(F.data.startswith("reject_user:"))
async def reject(query: CallbackQuery, bot: Bot):
    if not query.data:
        return

    user_id = int(query.data.split(":")[1])

    await bot.send_message(user_id, "❌ Твоя заявка отклонена.")

    message = query.message
    if not isinstance(message, Message):
        return

    await message.edit_reply_markup()
    await query.answer()
