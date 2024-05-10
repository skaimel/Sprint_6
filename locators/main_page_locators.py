from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_1 = (By.XPATH, ".//div[@id='accordion__heading-0']")
    QUESTION_2 = (By.XPATH, ".//div[@id='accordion__heading-1']")
    QUESTION_3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    QUESTION_4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    QUESTION_5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    QUESTION_6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    QUESTION_7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    QUESTION_8 = (By.XPATH, "//div[@id='accordion__heading-7']")
    ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
    ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-1']")
    ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-2']")
    ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-3']")
    ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-4']")
    ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-5']")
    ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-6']")
    ANSWER_8 = (By.XPATH, "//div[@id='accordion__panel-7']")