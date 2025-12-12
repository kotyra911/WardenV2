import hashlib
from bot.utils.logger import logger
from asyncio import run_coroutine_threadsafe
from bot.notifications import send_log_to_admin
from bot.main import bot
from services import loop_manager


def get_hash_value(combined_string):
    try:
        return hashlib.sha256(combined_string.encode()).hexdigest()
    except Exception as e:
        logger.error(f"ОШИБКА: {e}")

        run_coroutine_threadsafe(
            send_log_to_admin(bot),
            loop_manager.loop  # ← тут лежит loop
        )