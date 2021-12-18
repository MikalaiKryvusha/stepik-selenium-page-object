import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        object_page_main = MainPage(browser, link)
        object_page_main.open()
        object_page_main.go_to_login_page()
        object_login_page = LoginPage(browser, browser.current_url)
        object_login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        object_page_main = MainPage(browser, link)
        object_page_main.open()
        object_page_main.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    object_page_main = MainPage(browser, link)
    object_page_main.open()
    object_page_main.go_to_basket_page()
    object_page_basket = BasketPage(browser, link)
    object_page_basket.check_that_basket_is_empty()
    object_page_basket.check_that_there_is_basket_empty_text()