from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

microphone_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎤 Есть", callback_data="mic_yes"),
            InlineKeyboardButton(text="❌ Нет", callback_data="mic_no"),
        ]
    ]
)
