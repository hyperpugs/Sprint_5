# locators.py

from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
REGISTER_NAME_INPUT = (By.NAME, "name")  # Поле ввода имени на странице регистрации
REGISTER_EMAIL_INPUT = (By.NAME, "email")  # Поле ввода Email на странице регистрации
REGISTER_PASSWORD_INPUT = (By.NAME, "password")  # Поле ввода пароля на странице регистрации
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка отправки формы регистрации
REGISTER_ERROR_MESSAGE = (By.CLASS_NAME, "error-message")  # Сообщение об ошибке регистрации

# Локаторы для страницы входа
LOGIN_EMAIL_INPUT = (By.NAME, "email")  # Поле ввода email
LOGIN_PASSWORD_INPUT = (By.NAME, "password")  # Поле ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка входа

# Локаторы для основной страницы
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка «Войти в аккаунт» на главной
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(text(), 'Личный кабинет')]")  # Кнопка «Личный кабинет» на главной

# Локаторы для личного кабинета
PERSONAL_ACCOUNT_LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")  # Кнопка выхода в личном кабинете

# Локаторы для навигации и страницы восстановления пароля
CONSTRUCTOR_NAV_BUTTON = (By.XPATH, "//a[contains(text(), 'Конструктор')]")  # Кнопка «Конструктор»
STELLAR_BURGERS_LOGO = (By.CLASS_NAME, "stellar-burgers-logo")  # Логотип для главной страницы
REGISTER_PAGE_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка входа на странице регистрации
PASSWORD_RECOVERY_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка входа на странице восстановления пароля

# Локаторы для разделов конструктора
BUNS_SECTION_BUTTON = (By.XPATH, "//button[contains(text(), 'Булки')]")  # Кнопка перехода в раздел «Булки»
SAUCES_SECTION_BUTTON = (By.XPATH, "//button[contains(text(), 'Соусы')]")  # Кнопка перехода в раздел «Соусы»
FILLINGS_SECTION_BUTTON = (By.XPATH, "//button[contains(text(), 'Начинки')]")  # Кнопка перехода в раздел «Начинки»