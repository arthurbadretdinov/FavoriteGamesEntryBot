from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.config import CHAT_INVITE_LINK


def invite_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Войти в беседу", url=CHAT_INVITE_LINK)]
        ]
    )
