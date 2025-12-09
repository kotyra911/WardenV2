from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from bot.utils.logger import logger

def start_parse(driver, url:str):

    # Загрузка страницы
    logger.info(f"\nФункция start_parse(). Начал парсить по ссылке: {url}")
    try:
        logger.info(f"Загружаю страницу...")
        driver.get(url)  # Загрузка страницы
    except Exception as e:
        logger.error(f"\nПроизошла ошибка при загрузке страницы: {e}")

    # Получение всех объявлений
    try:
        logger.info(f"Пробую достать все объявления...")
        items = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        logger.debug(f"Количество собранных объявлений: {len(items)}")

        for item in items:
            avito_url = item.get_attribute("href")

            title = item.find_element(By.CSS_SELECTOR, "[itemprop='name']")

            block_photo = item.find_element(By.CSS_SELECTOR, ".photo-slider-list-item-r2YDC.photo-slider-dotsCounter-_n_4X")

            img = block_photo.find_element(By.TAG_NAME, "img")

            src = img.get_attribute("src")

            print(title.text)
            print(src)



    except Exception as e:
        logger.error(f"\nОшибка при попытке достать объявления со страницы: {e}")







