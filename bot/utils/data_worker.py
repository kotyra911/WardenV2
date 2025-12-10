from bot.utils.redis_interaction import RedisInteraction as rds
from bot.utils.security import get_hash_value
from bot.utils.logger import logger
from aiogram.utils.markdown import hlink
from bot.notifications import send_new_ad_to_user
from bot.config import TG_ID
from bot.main import bot

def start_data_working(avito_url: str, price: str, title: str, photo_url: str):
    logger.debug("Начал работу с данными")
    combined_string = avito_url + price + title + photo_url

    logger.debug("Хэширую строку")
    hash_value = get_hash_value(combined_string)

    logger.debug("Проверяю, нет ли совпадений в базе")
    if rds.check_hash_in_data_base(hash_value):

        logger.info("Запись обнаружена в базе. Перехожу к следующему")

    else:
        logger.debug("Добавляю запись в базу")
        rds.set_new_key(hash_value)
        # Вызов функции, для подготовки данных к отправке
        formatting_data_for_message(avito_url, price, title, photo_url)


def formatting_data_for_message(avito_url: str, price: str, title: str, photo_url: str):
    message = (
        f"<b>{price}</b>\n"        # жирная цена
        f"{title}\n\n"
        f'<a href="{avito_url}">Перейти</a>'
    )

    send_new_ad_to_user(TG_ID, bot, message, photo_url)
    return message, photo_url
