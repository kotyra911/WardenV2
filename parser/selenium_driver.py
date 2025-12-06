
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bot.config import AVITO_URL, CHROME_DRIVER_PATH



service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

#https://vk.cc/cS1Ais
