from pages.base_page import *
from conftest import *
from data import *


@allure.story('Тесты переходов по логотипу Яндекс/Самокат')
class TestLogoTransition:
    @allure.title('Тест перехода со страницы заказа на главую по клику на логотип "Самокат"')
    def test_logo_scooter(self, get_driver, get_order_page):
        get_order_page.open()
        get_order_page.click_on_yandex_logo()
        assert get_order_page.get_url() == Url.MAIN_PAGE

    @allure.title('Тест перехода со страницы заказа на страницу Дзен по клику на логотип "Яндекс"')
    def test_logo_yandex(self, get_driver, get_order_page):
        get_order_page.open()
        get_order_page.click_on_scooter_logo()
        assert Url.DZEN_PAGE in get_order_page.get_url()