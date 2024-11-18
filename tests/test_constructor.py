from locators import *
from conftest import *
from config import BASE_URL
def test_to_constructor(setup_browser):
        driver = setup_browser
        driver.get(BASE_URL)

        bun = driver.find_element(*BUN)
        assert "Флюоресцентная булка R2-D3" in bun.text

        driver.find_element(*SAUCES_SECTION_BUTTON).click()
        sauce = driver.find_element(*SAUCE)
        assert "Соус Spicy-X" in sauce.text

        driver.find_element(*FILLINGS_SECTION_BUTTON).click()
        filling = driver.find_element(*FILLING)
        assert "Мясо бессмертных моллюсков Protostomia" in filling.text