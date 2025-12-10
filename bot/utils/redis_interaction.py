from services.redis_connection import r
from bot.config import TTL_SECONDS as TTL
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
            return False
