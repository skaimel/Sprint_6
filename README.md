Файлы:

allure_results/ - Директория с отчетами о тестировании

locators/ - Директория с локаторами

pages/ - Директория с методами

tests/ - Директория с тестами

conftest - Модуль фикстур проекта

data - Модуль с данными

requirements.txt - Модуль с внешними зависимостями

Запуск тестов
pytest tests --alluredir=allure_results

Запуск отчетности allure
allure serve allure_results

