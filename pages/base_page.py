from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def get_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return element

    def get_element_text(self, how, what):
        try:
            element_text = self.browser.find_element(how, what).text
        except (NoSuchElementException):
            return False
        return element_text

    def is_element_with_text_present(self, how, what, text):
        try:
            elements = self.browser.find_elements(how, what)
            for element in elements:
                if element.text == text:
                    return True
            raise Exception(f"There is No such element '{what}' with text '{text}'")
        except (NoSuchElementException):
            return False

    def click_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element.click()
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")