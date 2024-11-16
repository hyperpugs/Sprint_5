
import pytest
from selenium import webdriver


@pytest.fixture
def setup_browser():
    """
    Фикстура для настройки и запуска веб-драйвера Chrome.
    """
    # Настройка веб-драйвера Chrome с использованием webdriver-manager для автоматической установки
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # Установка неявного ожидания для поиска элементов
    yield driver  # Передача драйвера в тесты
    driver.quit()  # Закрытие браузера по окончании теста