from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):

    def check_that_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), f"Element {BasketPageLocators.BASKET_ITEMS[1]} is presented"

    def check_that_there_is_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), f"Element {BasketPageLocators.BASKET_IS_EMPTY_TEXT[1]} is not presented"