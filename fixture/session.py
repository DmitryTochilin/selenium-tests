import requests
from random import randint
from selenium.common.exceptions import NoSuchElementException

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def response_code(self):
        response = requests.get(url=self.app.wd.current_url, verify=False)
        assert (str(response) == "<Response [200]>")

    def find(self, locator):
        return self.app.wd.find_element(*locator)

    def send_keys(self, locator, keys):
        element = self.app.wd.find_element(*locator)
        element.send_keys(keys)

    def close_cookies_notification(self):
        self.app.wd.find_element(*self.app.common_locators.CLOSE_COOKIES_NOTIFICATION).click()

    def click(self, locator):
        return self.app.wd.find_element(*locator).click()

    def assert_is_not_displayed(self, locator):
        try:
            self.find(locator)
            raise AssertionError("Element is displayed on page")
        except NoSuchElementException:
            pass

    def random_value(self):
        value = randint(1, 999)
        return value

    def assert_element_is_selected(self, app, locator):
        selected_atr = app.wd.find_element(*locator).get_attribute("selected")
        assert (selected_atr == "true")