from bot.config import AVITO_URL
from parser.avito_parser import start_parse
from parser.selenium_driver import driver
import threading
import time
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from config import BOT_TOKEN
from notify import router as notify_router

import threading
import asyncio
from aiogram import Bot, Dispatcher

# функция для запуска бота в лупе
def run_parser_loop():
    while True:
        start_parse(driver, AVITO_URL)
        time.sleep(30)  # пауза между парсингами, чтобы не перегружать CPU и сайт


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    # Подключение роутера
    dp.include_router(notify_router)

    # запускаем парсер в отдельном потоке
    threading.Thread(target=run_parser_loop, daemon=True).start()

    await dp.start_polling(bot)
