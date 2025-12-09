from bot.config import AVITO_URL
from parser.avito_parser import start_parse
from parser.selenium_driver import driver
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import Router

from config import BOT_TOKEN



start_parse(driver, AVITO_URL)