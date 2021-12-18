from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    object_page_main = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    object_page_main.open()                      # открываем страницу
    object_page_main.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина