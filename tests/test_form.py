import pytest
import allure
from pages.form_page import FormPage


@allure.feature("Форма заполнения")
@allure.story("Пользователь заполняет форму и отправляет данные")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_form(driver):
    form_page = FormPage(driver)

    with allure.step("Открываем страницу формы"):
        form_page.open()

    with allure.step("Заполняем имя"):
        form_page.fill_name("John Doe")

    with allure.step("Заполняем пароль"):
        form_page.fill_password("SecurePass123")

    with allure.step("Выбираем напитки"):
        form_page.select_drinks()

    with allure.step("Выбираем цвет"):
        form_page.select_color()

    with allure.step("Выбираем 'Yes' в поле 'Do you like automation?'"):
        form_page.select_automation()

    with allure.step("Заполняем email"):
        form_page.fill_email("john.doe@example.com")

    with allure.step("Заполняем сообщение"):
        form_page.fill_message()

    with allure.step("Нажимаем кнопку Submit"):
        form_page.submit_form()

    with allure.step("Проверяем сообщение в алерте"):
        alert_text = form_page.check_alert_message()
        assert alert_text == "Message received!", f"Ожидали 'Message received!', но получили '{alert_text}'"
