from bot.config import AVITO_URL
from parser.avito_parser import start_parse

from parser.selenium_driver import driver

start_parse(driver, AVITO_URL)
