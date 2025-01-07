from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import pytest

# Dekorator
def log_start_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        print(f"Test funksiyası {func.__name__} {start_time.strftime('%Y-%m-%d %H:%M:%S')}-də başlayır.")
        return func(*args, **kwargs)
    return wrapper

# Test funksiyası
@log_start_time
def test_web_elements():
    chrome_options = Options()
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")

    element1 = driver.find_element(By.CLASS_NAME, 'login-form__field-row')
    assert element1.value_of_css_property("width") == "372px"

    element2 = driver.find_element(By.CLASS_NAME, 'login-form__field-row')
    assert element2.value_of_css_property("height") == "40px"

    element2 = driver.find_element(By.CLASS_NAME, 'align__cell')
    assert element2.value_of_css_property("width") == "133.688px"

    element2 = driver.find_element(By.CLASS_NAME, 'login-form__container')
    assert element2.value_of_css_property("font-family") == "sans-serif"

    driver.quit()
