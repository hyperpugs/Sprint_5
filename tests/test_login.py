# tests/test_login.py

import pytest
from selenium import webdriver
from locators import *


def test_login_via_main_button(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # Проверка успешного входа
    assert "Личный кабинет" in driver.title


def test_login_via_personal_account_button(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    assert "Личный кабинет" in driver.title


def test_login_via_registration_page(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*REGISTER_PAGE_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    assert "Личный кабинет" in driver.title


def test_login_via_password_recovery_page(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    driver.find_element(*PASSWORD_RECOVERY_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    assert "Личный кабинет" in driver.title