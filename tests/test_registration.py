# tests/test_registration.py

import pytest
from locators import *  # Убедитесь, что импортируете ваши локаторы

def test_successful_registration(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Александр Жуков")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    assert "Привет, Александр!" in driver.page_source

def test_registration_invalid_password(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Александр Жуков")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    error_message = driver.find_element(*REGISTER_ERROR_MESSAGE).text
    assert "Пароль должен содержать не менее 6 символов" in error_message