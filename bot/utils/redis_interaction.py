from services import loop_manager
from services.redis_connection import r
from bot.config import TTL_SECONDS as TTL
from asyncio import run_coroutine_threadsafe
from bot.notifications import send_log_to_admin
from bot.main import bot
from bot.utils.logger import logger


class RedisInteraction:
    # Функция для проверки, существует ли ключ
    @staticmethod
    def check_hash_in_data_base(hash_value: str) -> bool:

        # Возвращает 1 если ключ существует.
        # Возвращает 0 если не существует.
        return r.exists(hash_value)

    @staticmethod
    def set_new_key(hash_value: str):

        try:

            r.set(hash_value, hash_value, ex=TTL)
            return True


        except Exception as e:

            logger.error(f"ОШИБКА: {e}")

            run_coroutine_threadsafe(

                send_log_to_admin(bot),

                loop_manager.loop  # ← тут лежит loop

            )
            return False


