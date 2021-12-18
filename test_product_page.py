import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
import faker

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    object_product_page = ProductPage(browser, link)
    object_product_page.open()
    object_product_page.should_not_be_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    object_product_page = ProductPage(browser, link)
    object_product_page.open()
    object_product_page.click_add_to_basket_button()
    object_product_page.solve_quiz_and_get_code()
    object_product_page.check_that_product_name_is_displayed_in_alert()
    object_product_page.check_that_total_basket_price_is_displayed_in_alert()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    object_product_page = ProductPage(browser, link)
    object_product_page.open()
    object_product_page.click_add_to_basket_button()
    object_product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    object_product_page = ProductPage(browser, link)
    object_product_page.open()
    object_product_page.click_add_to_basket_button()
    object_product_page.should_not_be_success_message_because_it_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    object_product_page = ProductPage(browser, link)
    object_product_page.open()
    object_product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    object_product_page = ProductPage(browser, link)
    object_product_page.open()
    object_product_page.should_be_login_link()
    object_product_page.go_to_login_page()
    object_login_page = LoginPage(browser, link)
    object_login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    object_product_page = ProductPage(browser, link)
    object_product_page.open()
    object_product_page.go_to_basket_page()
    object_basket_page = BasketPage(browser, link)
    object_basket_page.check_that_there_is_basket_empty_text()
    object_basket_page.check_that_basket_is_empty()

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        object_main_page = MainPage(browser, link)
        object_main_page.open()
        object_main_page.go_to_login_page()
        object_login_page = LoginPage(browser, link)
        object_login_page.should_be_login_page()

        object_faker = faker.Faker()
        email = str(time.time()).replace(".", "") + object_faker.email()
        password = "Qq1234567890"

        object_login_page.register_new_user(email=email,
                                            password=password)
        object_login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        object_product_page = ProductPage(browser, link)
        object_product_page.open()
        object_product_page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self, browser, link):
        object_product_page = ProductPage(browser, link)
        object_product_page.open()
        object_product_page.click_add_to_basket_button()
        object_product_page.solve_quiz_and_get_code()
        object_product_page.check_that_product_name_is_displayed_in_alert()
        object_product_page.check_that_total_basket_price_is_displayed_in_alert()