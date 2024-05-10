import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import *


class OrderPage(BasePage):
    @allure.step('Заполнение формы "Для кого самокат"')
    def client_form(self, data):
        self.wait_and_send_input(OrderPageLocators.NAME_INPUT, data.name)
        self.wait_and_send_input(OrderPageLocators.SURNAME_INPUT, data.surname)
        self.wait_and_send_input(OrderPageLocators.ADDRESS_INPUT, data.address)
        self.wait_and_send_input(OrderPageLocators.SUBWAY_INPUT, data.subway)
        self.wait_and_click_element(OrderPageLocators.SELECT_SUBWAY)
        self.wait_and_send_input(OrderPageLocators.PHONE_NUMBER_INPUT, data.phone_number)
        self.wait_and_click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение формы "Про аренду"')
    def rent_form(self, data):
        self.wait_and_send_input(OrderPageLocators.DATE_DELIVERY, data.date)
        self.wait_and_click_element(OrderPageLocators.SELECT_COLOR_GREY)
        self.wait_and_click_element(OrderPageLocators.RENT_PERIOD)
        self.wait_and_click_element(OrderPageLocators.RENT_PERIOD_ONE_DAY)
        self.wait_and_send_input(OrderPageLocators.COMMENT_INPUT, data.comment)
        self.wait_and_click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Проверка успешного оформления заказа')
    def order_issued_check(self):
        return self.get_text(OrderPageLocators.ORDER_COMPLETED)

    @allure.step('Переход по лого Яндекс')
    def click_on_yandex_logo(self):
        self.wait_and_click_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step('Переход по лого Самокат')
    def click_on_scooter_logo(self):
        self.wait_and_click_element(BasePageLocators.LOGO_YANDEX)
        self.tab_switch(DzenLocators.DZEN_LOGO)