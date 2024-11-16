
from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
REGISTER_NAME_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода имени на странице регистрации
REGISTER_EMAIL_INPUT = (By.XPATH, "//fieldset[2]/div/div/input") # Поле ввода Email на странице регистрации
REGISTER_PASSWORD_INPUT = (By.XPATH, "//fieldset[3]/div/div/input")  # Поле ввода пароля на странице регистрации
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//div/main/div/form/button")  # Кнопка отправки формы регистрации
REGISTER_ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  # Сообщение об ошибке
REGISTER_FAIL_MESSAGE = (By.XPATH, '//div/main/div/p')
REGISTER_INVALID_PASS = (By.XPATH, '//fieldset[3]/div/p') # Некорректный пароль
# Локаторы для страницы входа
LOGIN_EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")  # Поле ввода email
LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка входа
PERSONAL_ACCOUNT = (By.XPATH, "//div/header/nav/a/p")
# Локаторы для основной страницы
MAIN_LOGIN_BUTTON = (By.XPATH, "//section[2]/div/button[text()= 'Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a/p[text()='Личный Кабинет']")  # Кнопка «Личный кабинет» на главной

# Локаторы для личного кабинета
PERSONAL_ACCOUNT_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка выхода в личном кабинете

# Локаторы для навигации и страницы восстановления пароля
CONSTRUCTOR_NAV_BUTTON = (By.XPATH, "//a/p[text()='Конструктор']")  # Кнопка «Конструктор»
STELLAR_BURGERS_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип для главной страницы
REGISTER_PAGE_LOGIN_BUTTON = (By.XPATH, "//a/p[text()='Войти']")  # Кнопка входа на странице регистрации
PASSWORD_RECOVERY_LOGIN_BUTTON = (By.XPATH, "//a/p[text()='Войти']")  # Кнопка входа на странице восстановления пароля

# Локаторы для разделов конструктора
BUNS_SECTION_BUTTON = (By.XPATH, "//span[text()='Булки']")  # Кнопка перехода в раздел «Булки»
SAUCES_SECTION_BUTTON = (By.XPATH, "//span[text()='Соусы']")  # Кнопка перехода в раздел «Соусы»
FILLINGS_SECTION_BUTTON = (By.XPATH, "//span[text()='Начинки']")  # Кнопка перехода в раздел «Начинки»