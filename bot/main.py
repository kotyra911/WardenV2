import threading
import time
import logging
import asyncio
from aiogram import Bot, Dispatcher
from parser.selenium_driver import driver
from config import AVITO_URL, BOT_TOKEN  # берём настройки из конфига

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# создаём объекты бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# функция для запуска парсера в цикле
def run_parser_loop():
    from parser.avito_parser import start_parse
    while True:
        try:
            logger.info("Запускаем start_parse()")
            start_parse(driver, AVITO_URL)
        except Exception as e:
            logger.error(f"Ошибка в парсере: {e}")
        logger.info("Пауза 30 секунд перед следующим запуском")
        time.sleep(30)

async def main():
    # запускаем парсер в отдельном потоке
    threading.Thread(target=run_parser_loop, daemon=True).start()

    # запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
