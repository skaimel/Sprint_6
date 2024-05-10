from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, ".//*[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//*[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_INPUT = (By.XPATH, ".//*[@placeholder='* Станция метро']")
    SELECT_SUBWAY = (By.XPATH, ".//*[@class='select-search__row']")
    PHONE_NUMBER_INPUT = (By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//*[text()='Далее']")
    DATE_DELIVERY = (By.XPATH, ".//*[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.XPATH, ".//*[text()='* Срок аренды']")
    RENT_PERIOD_ONE_DAY = (By.XPATH, ".//*[text()='сутки']")
    SELECT_COLOR_GREY = (By.XPATH, ".//*[@id='grey']")
    COMMENT_INPUT = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    ORDER_CONFIRM = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    BUTTON_YES = (By.XPATH, ".//*[text()='Да']")
    ORDER_COMPLETED = [By.XPATH, ".//div[text() = 'Заказ оформлен']"]