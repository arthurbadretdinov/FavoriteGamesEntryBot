from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def moderation_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✔ Принять", callback_data="accept"),
                InlineKeyboardButton(text="❌ Отклонить", callback_data="reject"),
            ]
        ]
    )
