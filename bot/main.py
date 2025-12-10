from bot.config import AVITO_URL
from parser.selenium_driver import driver
import threading
import time
from aiogram import Bot, Dispatcher, Router, types
from config import BOT_TOKEN
import threading
import asyncio
from aiogram import Bot, Dispatcher


bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# функция для запуска бота в лупе
def run_parser_loop():
    while True:
        from parser.avito_parser import start_parse
        start_parse(driver, AVITO_URL)
        time.sleep(30)  # пауза между парсингами, чтобы не перегружать сайт

async def main():

    # запускаем парсер в отдельном потоке
    threading.Thread(target=run_parser_loop, daemon=True).start()

    await dp.start_polling(bot)

