import threading
import time
import logging
import asyncio
from aiogram import Bot, Dispatcher
from parser.selenium_driver import driver
from config import AVITO_URL, BOT_TOKEN  # берём настройки из конфига
from services import loop_manager
from asyncio import run_coroutine_threadsafe
from bot.notifications import send_log_to_admin



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
            start_parse(driver, AVITO_URL)  # Основная цепочка парсинга

        except Exception as e:
            logger.error(f"ОШИБКА: {e}")

            run_coroutine_threadsafe(
                send_log_to_admin(bot),
                loop_manager.loop  # ← тут лежит loop
            )


        logger.info("Пауза 30 секунд перед следующим запуском")
        time.sleep(30)

loop = None

async def main():
    loop_manager.loop = asyncio.get_running_loop()  # ← сохраняем loop, чтобы можно было запустить асинхронную функцию в синхронном потоке

    threading.Thread(target=run_parser_loop, daemon=True).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

