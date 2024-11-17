
from selenium.webdriver.common.by import By


REGISTER_NAME_INPUT = (By.XPATH, "//input[@name='name']")
REGISTER_EMAIL_INPUT = (By.XPATH, "//fieldset[2]/div/div/input")
REGISTER_PASSWORD_INPUT = (By.XPATH, "//fieldset[3]/div/div/input")
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//div/main/div/form/button")
REGISTER_ERROR_MESSAGE = (By.CLASS_NAME, "input__error")
REGISTER_FAIL_MESSAGE = (By.XPATH, '//div/main/div/p')
REGISTER_INVALID_PASS = (By.XPATH, '//fieldset[3]/div/p')

# Локаторы для страницы входа
LOGIN_EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")
PERSONAL_ACCOUNT = (By.XPATH, "//div/header/nav/a/p")
MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
LOGIN_THROURGH_REGISTER =  (By.XPATH, "//div/p/a")


# Локаторы для основной страницы
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()= 'Войти в аккаунт']")
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a/p[text()='Личный Кабинет']")

# Локаторы для личного кабинета
PERSONAL_ACCOUNT_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
FROM_PERSONAL_ACC_TO_CONSTRUCTOR = (By.XPATH, "//li[1]/a/p[text()= 'Конструктор']")
FROM_PERSONAL_ACC_TO_MAIN_PAGE = (By.XPATH, "//div/a")

# Локаторы для навигации и страницы восстановления пароля
REGISTER_PAGE_LOGIN_BUTTON = (By.XPATH, "//a/p[text()='Выход']")
PASSWORD_RECOVERY_LOGIN_BUTTON = (By.XPATH, "//a/p[text()='Выход']")

# Локаторы для разделов конструктора
BUN = (By.XPATH, "//a[1]/p[text()='Флюоресцентная булка R2-D3']")
SAUCES_SECTION_BUTTON = (By.XPATH, "//div[1]/div[2]")
SAUCE = (By.XPATH, "//a[1]/p[text()= 'Соус Spicy-X']")
FILLINGS_SECTION_BUTTON = (By.XPATH, "//span[text()='Начинки']")
FILLING = (By.XPATH, "//a[1]/p[text()= 'Мясо бессмертных моллюсков Protostomia']")
MAKE_BURGER = (By.XPATH, "//section[1]/h1[text()= 'Соберите бургер']")
