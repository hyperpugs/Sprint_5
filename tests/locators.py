
from selenium.webdriver.common.by import By


REGISTER_NAME_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода имени на странице регистрации
REGISTER_EMAIL_INPUT = (By.XPATH, "//fieldset[2]/div/div/input") # Поле ввода Email на странице регистрации
REGISTER_PASSWORD_INPUT = (By.XPATH, "//fieldset[3]/div/div/input")  # Поле ввода пароля на странице регистрации
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//div/main/div/form/button")  # Кнопка отправки формы регистрации
REGISTER_ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  # Сообщение об ошибке
REGISTER_INVALID_PASS = (By.XPATH, '//fieldset[3]/div/p') # Некорректный пароль


# Локаторы для страницы входа
LOGIN_EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")  # Поле ввода email
LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка входа
PERSONAL_ACCOUNT = (By.XPATH, "//div/header/nav/a/p") # Кнопка Личного кабинета
MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка оформить заказ
LOGIN_THROURGH_REGISTER =  (By.XPATH, "//div/p/a") # Кнопка войти


# Локаторы для основной страницы
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()= 'Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a/p[text()='Личный Кабинет']")  # Кнопка «Личный кабинет» на главной

# Локаторы для личного кабинета
PERSONAL_ACCOUNT_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода в личном кабинете
FROM_PERSONAL_ACC_TO_CONSTRUCTOR = (By.XPATH, "//li[1]/a/p[text()= 'Конструктор']") #Кнопка Конструктор
FROM_PERSONAL_ACC_TO_MAIN_PAGE = (By.XPATH, "//div/a") # Кнопка перехода на главную

# Локаторы для навигации и страницы восстановления пароля
REGISTER_PAGE_LOGIN_BUTTON = (By.XPATH, "//a/p[text()='Выход']")  # Кнопка входа на странице регистрации
PASSWORD_RECOVERY_LOGIN_BUTTON = (By.XPATH, "//a/p[text()='Выход']")  # Кнопка входа на странице восстановления пароля

# Локаторы для разделов конструктора
BUN = (By.XPATH, "//a[1]/p[text()='Флюоресцентная булка R2-D3']") # Кнопка с булкой
SAUCES_SECTION_BUTTON = (By.XPATH, "//div[1]/div[2]")  # Кнопка перехода в раздел «Соусы»
SAUCE = (By.XPATH, "//a[1]/p[text()= 'Соус Spicy-X']") # Кнопка с соусом
FILLINGS_SECTION_BUTTON = (By.XPATH, "//span[text()='Начинки']")  # Кнопка перехода в раздел «Начинки»
FILLING = (By.XPATH, "//a[1]/p[text()= 'Мясо бессмертных моллюсков Protostomia']") # Кнопка с начинкой
MAKE_BURGER = (By.XPATH, "//section[1]/h1[text()= 'Соберите бургер']") # Кнопка для проверки
