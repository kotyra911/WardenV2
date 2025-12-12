from bot.utils.redis_interaction import RedisInteraction as rds
from bot.utils.security import get_hash_value
from bot.utils.logger import logger
from aiogram.utils.markdown import hlink
from bot.notifications import send_new_ad_to_user,send_log_to_admin
from bot.config import tg_ids
from bot.main import bot
import asyncio
from asyncio import run_coroutine_threadsafe
from services import loop_manager


def start_data_working(avito_url: str, price: str, title: str, photo_url: str, seller_id: str):

    try:
        logger.debug("Начал работу с данными")
        combined_string = price + title + photo_url


        logger.debug("Хэширую строку")
        hash_value = get_hash_value(combined_string)

        logger.debug("Проверяю, нет ли совпадений в базе")
        if rds.check_hash_in_data_base(hash_value):

            logger.info("Запись обнаружена в базе. Перехожу к следующему")

        else:
            logger.debug("Добавляю запись в базу")
            rds.set_new_key(hash_value)
            # Вызов функции, для подготовки данных к отправке
            formatting_data_for_message(avito_url, price, title, photo_url, seller_id)

    except Exception as e:
        logger.error(f"ОШИБКА: {e}")

        run_coroutine_threadsafe(
            send_log_to_admin(bot),
            loop_manager.loop  # ← тут лежит loop
        )


def formatting_data_for_message(avito_url: str, price: str, title: str, photo_url: str, seller_id: str):

    try:
        message = (
            f"<b>{price}</b>\n"        # жирная цена
            f"{title}\n\n"
            f'ID продавца: {seller_id}\n\n'
            f'<a href="{avito_url}">Перейти</a>'

        )
        # отправляем корутину в event loop главного потока
        run_coroutine_threadsafe(
            send_new_ad_to_user(bot, message, photo_url),
            loop_manager.loop  # ← тут лежит loop
        )

        return message, photo_url

    except Exception as e:
        logger.error(f"ОШИБКА: {e}")

        run_coroutine_threadsafe(
            send_log_to_admin(bot),
            loop_manager.loop  # ← тут лежит loop
        )



