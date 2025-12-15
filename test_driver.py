
from parser.selenium_driver import driver
import time

try:
    driver.get("google.com")
    print("Браузер открылся!")
    time.sleep(10)  # оставляем окно открытым, чтобы проверить
finally:
    driver.quit()
    print("Драйвер закрыт")
