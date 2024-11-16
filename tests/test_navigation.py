
from selenium import webdriver
from locators import *


def test_logout_from_personal_account(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_LOGOUT_BUTTON).click()
    assert "Вы успешно вышли" in driver.page_source


def test_navigation_to_constructor(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/account")

    driver.find_element(*CONSTRUCTOR_NAV_BUTTON).click()
    assert "Конструктор" in driver.title

    driver.find_element(*STELLAR_BURGERS_LOGO).click()
    assert "Главная" in driver.title


def test_constructor_sections(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/constructor")

    driver.find_element(*BUNS_SECTION_BUTTON).click()
    assert "Булки" in driver.page_source

    driver.find_element(*SAUCES_SECTION_BUTTON).click()
    assert "Соусы" in driver.page_source

    driver.find_element(*FILLINGS_SECTION_BUTTON).click()
    assert "Начинки" in driver.page_source