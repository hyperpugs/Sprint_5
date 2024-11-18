import pytest
from locators import *
from conftest import *
from config import BASE_URL, REGISTER_URL, FORGOT_URL
def test_login_via_main_button(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    account = driver.find_element(*PERSONAL_ACCOUNT)
    assert "Личный Кабинет" in account.text


def test_login_via_personal_account_button(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    order = driver.find_element(*MAKE_ORDER)

    assert "Оформить заказ" in order.text


def test_login_via_registration_page(setup_browser):
    driver = setup_browser
    driver.get(REGISTER_URL)

    driver.find_element(*LOGIN_THROURGH_REGISTER).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    order = driver.find_element(*MAKE_ORDER)

    assert "Оформить заказ" in order.text


def test_login_via_password_recovery_page(setup_browser):
    driver = setup_browser
    driver.get(FORGOT_URL)

    driver.find_element(*LOGIN_THROURGH_REGISTER).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    order = driver.find_element(*MAKE_ORDER)

    assert "Оформить заказ" in order.text

def test_registration_invalid_password(setup_browser):
    driver = setup_browser
    driver.get(REGISTER_URL)

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Александр Жуков")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    error_message = driver.find_element(*REGISTER_ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_message