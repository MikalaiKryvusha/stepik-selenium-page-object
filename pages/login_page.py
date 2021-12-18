from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        reg_email_field = self.get_element(*LoginPageLocators.REG_EMAIL_INPUT_FIELD), f"Element {LoginPageLocators.REG_EMAIL_INPUT_FIELD[1]} is not presented"
        reg_pass1_field = self.get_element(*LoginPageLocators.REG_PASSWORD_1_INPUT_FIELD), f"Element {LoginPageLocators.REG_PASSWORD_1_INPUT_FIELD[1]} is not presented"
        reg_pass2_field = self.get_element(*LoginPageLocators.REG_PASSWORD_2_INPUT_FIELD), f"Element {LoginPageLocators.REG_PASSWORD_2_INPUT_FIELD[1]} is not presented"
        self.send_keys_into_element(*LoginPageLocators.REG_EMAIL_INPUT_FIELD, email)
        self.send_keys_into_element(*LoginPageLocators.REG_PASSWORD_1_INPUT_FIELD, password)
        self.send_keys_into_element(*LoginPageLocators.REG_PASSWORD_2_INPUT_FIELD, password)
        self.click_element(*LoginPageLocators.REG_BUTTON)
        pass

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        login_sub_string = "login"
        assert login_sub_string in current_url, f"Substring '{login_sub_string}' is not in URL 'current_url'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT_FIELD), f"Element {LoginPageLocators.LOGIN_EMAIL_INPUT_FIELD[1]} is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT_FIELD), f"Element {LoginPageLocators.LOGIN_PASSWORD_INPUT_FIELD[1]} is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_INPUT_FIELD), f"Element {LoginPageLocators.REG_EMAIL_INPUT_FIELD[1]} is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_1_INPUT_FIELD), f"Element {LoginPageLocators.REG_PASSWORD_1_INPUT_FIELD[1]} is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_2_INPUT_FIELD), f"Element {LoginPageLocators.REG_PASSWORD_2_INPUT_FIELD[1]} is not presented"
