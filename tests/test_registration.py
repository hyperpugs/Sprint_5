import re
from locators import *
from conftest import *
from config import REGISTER_URL
def test_successful_registration(setup_browser):
    driver = setup_browser
    driver.get(REGISTER_URL)

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Александр Жуков")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()
    registration = driver.find_element(*REGISTER_SUBMIT_BUTTON)

    assert registration is not None and "Зарегистрироваться" in registration.text

def is_valid_email(email):
    email = "aleksandr_zhukov_15_777@yandex.ru"
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def test_already_registred(setup_browser):
    driver = setup_browser
    driver.get(REGISTER_URL)

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Александр Жуков")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()
    already_registred = driver.find_element(*ALREADY_REGISTRED)
    assert "Такой пользователь уже существует" in already_registred.text

def test_registration_with_short_password(setup_browser):
    driver = setup_browser  # или другой драйвер
    driver.get(REGISTER_URL)

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Руслан")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("alex_bug_15_003@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("qw124")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()
    error_message = driver.find_element(*REGISTER_INVALID_PASS)
    assert error_message is not None and "Некорректный пароль" in error_message.text
