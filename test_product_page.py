import time
import pytest
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    object_shellcoders_handbook_page = ProductPage(browser, link)
    object_shellcoders_handbook_page.open()
    object_shellcoders_handbook_page.click_add_to_basket_button()
    object_shellcoders_handbook_page.solve_quiz_and_get_code()
    object_shellcoders_handbook_page.check_that_product_name_is_displayed_in_alert()
    object_shellcoders_handbook_page.check_that_total_basket_price_is_displayed_in_alert()
    time.sleep(1)