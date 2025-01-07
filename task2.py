import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Fikstura: Selenium sürücüsü
@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.quit()

# Fikstura: Elementlərin yüklənməsi
@pytest.fixture(scope="module")
def elements(driver):
    return {
        "field_row": driver.find_element(By.CLASS_NAME, 'login-form__field-row'),
        "align_cell": driver.find_element(By.CLASS_NAME, 'align__cell'),
        "container": driver.find_element(By.CLASS_NAME, 'login-form__container')
    }

# Testlər
def test_field_row_width(elements):
    assert elements["field_row"].value_of_css_property("width") == "372px"

def test_field_row_height(elements):
    assert elements["field_row"].value_of_css_property("height") == "40px"

def test_align_cell_width(elements):
    assert elements["align_cell"].value_of_css_property("width") == "133.688px"

def test_container_font(elements):
    assert elements["container"].value_of_css_property("font-family") == "sans-serif"

def test_container_background(elements):
    assert elements["container"].value_of_css_property("background-color") == "rgba(255, 255, 255, 1)"
