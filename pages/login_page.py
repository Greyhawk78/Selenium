import time

from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Login url is not present'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        time.sleep(5)
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASS1)
        password_field.send_keys(password)
        password_field = self.browser.find_element(*LoginPageLocators.PASS2)
        password_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON)
        button.click()
