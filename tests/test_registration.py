# tests/test_registration.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest
from locators import *  # Убедитесь, что импортируете ваши локаторы

def test_successful_registration(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Александр Жуков")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    assert "Зарегистрироваться" in driver.find_element(By.XPATH, '//div/main/div/form/button').text

def test_already_registred(setup_browser):
    driver = setup_browser
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Александр Жуков")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("aleksandr_zhukov_15_777@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    assert "Такой пользователь уже существует" in driver.find_element(By.XPATH,'//div/main/div/p').text

def test_registration_with_short_password(setup_browser):
    driver = setup_browser  # или другой драйвер
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполнение формы с некорректным паролем
    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Руслан")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("alex_bug_15_003@yandex.ru")
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("qw124")  # пароль короче 6 символов
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    # Проверка появления ошибки
    error_message = driver.find_element(*REGISTER_INVALID_PASS)
    assert error_message is not None and "Некорректный пароль" in error_message.text

