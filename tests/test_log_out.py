from locators import *
from conftest import *
from config import BASE_URL
def test_forward_to_personal_account(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT).click()
    driver.find_element(*PERSONAL_ACCOUNT_LOGOUT_BUTTON).click()
    enter = driver.find_element(*LOGIN_SUBMIT_BUTTON)

    assert "Войти" in enter.text