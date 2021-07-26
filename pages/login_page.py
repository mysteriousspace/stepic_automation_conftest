from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1, "this is not login page"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, "There is no LogIn form"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.browser.find_element(*LoginPageLocators.REGISTERED_FORM)
        assert True, "There is no Registration form"
