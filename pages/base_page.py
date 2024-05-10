import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from data import Url


class BasePage:
    def __init__(self, driver, url_path):
        self.driver = driver
        url = Url.MAIN_PAGE
        self.url = url + url_path

    @allure.step('Открытие браузера на заданный URL')
    def open(self):
        url = self.url
        self.driver.get(url)

    @allure.step('Текущий URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Ожидание появления элемента')
    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание и клик по элементу')
    def wait_and_click_element(self, locator):
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(locator)).click()

    @allure.step('Скроллим страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ожидание элемента и ввод данных')
    def wait_and_send_input(self, locator, data):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(locator))
        return self.driver.find_element(*locator).send_keys(data)

    @allure.step('Принять куки')
    def accept_cookies(self):
        return self.wait_and_click_element(BasePageLocators.ACCEPT_COOKIES)

    @allure.step('Ожидание и получение текста элемента')
    def get_text(self, locator):
        return WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(locator)).text

    @allure.step('Переключение на открытый при переходе таб')
    def tab_switch(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(locator))