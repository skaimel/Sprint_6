import allure
import pytest
from conftest import *
from data import *
from locators.main_page_locators import *


@allure.story('Тесты выпадающего списка "Вопросы о важном"')
class TestDropDownList:
    @allure.title('Тест соответствия текста ответа')
    @pytest.mark.parametrize('question, answer, answer_text', [
        [MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, AnswerText.answer_text_1],
        [MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, AnswerText.answer_text_2],
        [MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, AnswerText.answer_text_3],
        [MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, AnswerText.answer_text_4],
        [MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, AnswerText.answer_text_5],
        [MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, AnswerText.answer_text_6],
        [MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, AnswerText.answer_text_7],
        [MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, AnswerText.answer_text_8]
    ])
    def test_drop_down_text(self, get_driver, get_main_page, question, answer, answer_text):
        get_main_page.open()
        get_main_page.accept_cookies()
        get_main_page.scroll_to_bottom()
        get_main_page.click(question)
        assert get_main_page.get_text(answer) == answer_text