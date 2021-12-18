from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_1_INPUT_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2_INPUT_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOLD_TEXT_IN_ALERTS = (By.CSS_SELECTOR, ".alert-success > .alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, ".alert-info")
    BASKET_TOTAL_BOLD_TEXT = (By.CSS_SELECTOR, ".alert-info strong")




