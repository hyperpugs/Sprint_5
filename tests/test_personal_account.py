
from selenium import webdriver
from locators import *

def test_forward_to_personal_account(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT).click()
    exit = driver.find_element(*PERSONAL_ACCOUNT_LOGOUT_BUTTON)

    assert "Выход" in exit.text

def test_transfer_to_constructor(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT).click()
    driver.find_element(*FROM_PERSONAL_ACC_TO_CONSTRUCTOR).click()
    burger = driver.find_element(*MAKE_BURGER)

    assert "Соберите бургер" in burger.text

def test_trasfer_to_main_page(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT).click()
    driver.find_element(*FROM_PERSONAL_ACC_TO_MAIN_PAGE).click()
    main = driver.find_element(*MAKE_BURGER)

    assert "Соберите бургер" in main.text

