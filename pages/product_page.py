from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), f"Element {ProductPageLocators.ADD_TO_BASKET_BUTTON[1]} is not presented"
        self.click_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def check_that_product_name_is_displayed_in_alert(self):
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        assert self.is_element_with_text_present(*ProductPageLocators.BOLD_TEXT_IN_ALERTS, product_name), f"Element {ProductPageLocators.BOLD_TEXT_IN_ALERTS[1]} with text '{product_name}' is not presented"

    def check_that_total_basket_price_is_displayed_in_alert(self):
        product_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        assert self.is_element_with_text_present(*ProductPageLocators.BASKET_TOTAL_BOLD_TEXT, product_price), f"Element {ProductPageLocators.BOLD_TEXT_IN_ALERTS[1]} with text '{product_price}' is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_because_it_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"