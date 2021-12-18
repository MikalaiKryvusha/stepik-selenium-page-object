from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_1_INPUT_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2_INPUT_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")