import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Url


@pytest.fixture(scope='function')
def get_driver():
    driver = webdriver.Firefox()

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def get_main_page(get_driver):
    url_path = ''
    return MainPage(get_driver, url_path)


@pytest.fixture(scope='function')
def get_order_page(get_driver):
    url_path = Url.ORDER_PATH
    return OrderPage(get_driver, url_path)