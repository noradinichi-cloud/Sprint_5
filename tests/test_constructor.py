from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from locators import MainPageLocators


class TestConstructor:
    def test_switch_to_sauces_tab(self, driver):
        driver.get(Urls.BASE_URL)
        sauces_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        )
        sauces_tab.click()
        assert "tab_type_current" in sauces_tab.get_attribute("class")

    def test_switch_to_fillings_tab(self, driver):
        driver.get(Urls.BASE_URL)
        fillings_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)
        )
        fillings_tab.click()
        assert "tab_type_current" in fillings_tab.get_attribute("class")

    def test_switch_to_buns_tab(self, driver):
        driver.get(Urls.BASE_URL)
        sauces_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        )
        sauces_tab.click()

        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)
        buns_tab.click()
        assert "tab_type_current" in buns_tab.get_attribute("class")
