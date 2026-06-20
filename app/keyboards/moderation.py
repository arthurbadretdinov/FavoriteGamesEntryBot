from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def moderation_kb(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Принять", callback_data=f"approve_user:{user_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Отказать", callback_data=f"reject_user:{user_id}"
                ),
            ]
        ]
    )
