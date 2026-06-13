import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

async def main():
    token = os.getenv("BOT_TOKEN")
    
    if not token:
        raise ValueError("BOT_TOKEN is not set in .env")
    
    bot = Bot(token=token)
    dp = Dispatcher()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())