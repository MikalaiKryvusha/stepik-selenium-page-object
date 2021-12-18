from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    object_page_main = MainPage(browser, link)
    object_page_main.open()
    object_page_main.go_to_login_page()
    object_login_page = LoginPage(browser, browser.current_url)
    object_login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    object_page_main = MainPage(browser, link)
    object_page_main.open()
    object_page_main.should_be_login_link()