import asyncio
import threading
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

global integer
integer = 0


async def wait(time):
    await asyncio.sleep(time)


def join(code, user):
    global integer
    _options = uc.ChromeOptions()
    _options.add_argument("--disable-logging")
    _options.add_argument("--no-sandbox")
    _options.add_argument("--disable-dev-shm-usage")
    _options.add_argument("--incognito")
    _options.add_argument("--lang=en")
    _options.add_argument("--FontRenderHinting[none]")

    driver = uc.Chrome(options=_options)

    driver.get("https://kahoot.it")
    field = driver.find_element(By.XPATH, "html/body/div/div[1]/div/div[3]/div[2]/main/div/form/input")
    field.send_keys(code)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[3]/div[2]/main/div/form/button").click()
    asyncio.run(wait(0.5))
    integer = int(integer) + int(1)
    user = user + str(integer)
    driver.find_element(By.XPATH, "html/body/div/div[1]/div/div[3]/div[2]/main/div/form/input").send_keys(user)
    asyncio.run(wait(0.1))
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[3]/div[2]/main/div/form/button").click()
    driver.minimize_window()
    asyncio.run(wait(600))
