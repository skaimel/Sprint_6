import allure
import pytest

from conftest import *
from data import *
from locators.order_page_locators import *
from locators.base_page_locators import *


@allure.story('Тесты заказа самоката')
class TestScooterOrder:
    @allure.title('Позитивный тест заказа самоката')
    @pytest.mark.parametrize('button, data', [(BasePageLocators.ORDER_BUTTON_UP, User1),
                                              (BasePageLocators.ORDER_BUTTON_DOWN, User2)])
    def test_scooter_order(self, get_driver, button, data, get_order_page, get_main_page):
        get_main_page.open()
        get_order_page.accept_cookies()
        get_order_page.wait_and_click_element(button)
        get_order_page.client_form(data)
        get_order_page.rent_form(data)
        get_order_page.wait_and_click_element(OrderPageLocators.BUTTON_YES)
        assert 'Заказ оформлен' in get_order_page.order_issued_check()