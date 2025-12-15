import time
from selenium.webdriver.common.by import By
from bot.utils.logger import logger
from bot.utils.data_worker import start_data_working
from bot.config import sellers_black_list
from asyncio import run_coroutine_threadsafe
from bot.notifications import send_log_to_admin
from bot.main import bot
from services import loop_manager


def start_parse(driver, url:str):

    # Загрузка страницы
    logger.info(f"\nФункция start_parse(). Начал парсить по ссылке: {url}")
    try:
        logger.info(f"Загружаю страницу...")
        driver.get(url)  # Загрузка страницы
        time.sleep(5)  # Пауза, чтобы подгрузились картинки
    except Exception as e:
        logger.error(f"ОШИБКА: {e}")

        run_coroutine_threadsafe(
            send_log_to_admin(bot),
            loop_manager.loop  # ← тут лежит loop
        )

    # Получение всех объявлений
    try:
        logger.info(f"Пробую достать все объявления...")
        items = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        logger.debug(f"Количество собранных объявлений: {len(items)}")

        count=0  # Счетчик, чтобы брать только первые 5 объявлений

        for item in items:


            # Скроллинг вниз, для загрузки всех фотографий
            driver.execute_script("arguments[0].scrollIntoView(true);", item)
            time.sleep(0.3)  # Передышка, чтобы новые данные успевали подгружаться

            # Поиск элемента, который содержит цену
            price_el = item.find_element(By.CSS_SELECTOR, "span.styles-module-size_l-kPWfk")
            price = price_el.text

            # Поиск элемента, который содержит ссылку на объявление
            link_el = item.find_element(By.CSS_SELECTOR, "a")
            avito_url = link_el.get_attribute("href")

            # Заголовок объявления
            title = item.find_element(By.CSS_SELECTOR, "[itemprop='name']").text

            # Изъятие фотографии
            block_photo = item.find_element(By.CSS_SELECTOR, "[class='photo-slider-list-R0jle']")
            img = block_photo.find_element(By.TAG_NAME, "img")
            photo_url = img.get_attribute("src")

            sid = str(item.get_attribute("data-item-id"))  # Достаем id продавца
            seller_id = sid[0:4]  # Берем только статичную часть

            # Проверяем, есть ли продавец в черном списке
            if seller_id in sellers_black_list:
                continue  # Если есть, переходим к следующему объявлению
            else:
                print(seller_id)

                # Отправка данных дальше по цепочке
                start_data_working(avito_url, price, title, photo_url, seller_id)


    except Exception as e:
        logger.error(f"ОШИБКА: {e}")

        run_coroutine_threadsafe(
            send_log_to_admin(bot),
            loop_manager.loop  # ← тут лежит loop
        )








