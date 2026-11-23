from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TestUser, Urls
from locators import (
    ForgotPasswordPageLocators,
    LoginPageLocators,
    MainPageLocators,
    RegisterPageLocators,
)


class TestLogin:
    def _submit_login_form(self, driver):
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(TestUser.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestUser.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def test_login_via_main_page_button(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        self._submit_login_form(driver)

        order_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_btn.is_displayed()

    def test_login_via_personal_account_button(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self._submit_login_form(driver)

        order_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_btn.is_displayed()

    def test_login_via_register_page_link(self, driver):
        driver.get(Urls.REGISTER_URL)
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        self._submit_login_form(driver)

        order_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_btn.is_displayed()

    def test_login_via_forgot_password_page_link(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
        self._submit_login_form(driver)

        order_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_btn.is_displayed()
