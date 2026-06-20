import os
from dotenv import load_dotenv

load_dotenv()


def get_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"{name} is not set")
    return value


BOT_TOKEN: str = get_env("BOT_TOKEN")
ADMIN_CHAT_ID: int = int(get_env("ADMIN_CHAT_ID"))
CHAT_INVITE_LINK: str = get_env("CHAT_INVITE_LINK")
