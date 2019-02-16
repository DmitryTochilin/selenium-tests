from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fixture.locators import *

from fixture.session import SessionHelper
from pages.booking_widget import BookingWidget
from pages.main_page import MainPage


class Application:
    def __init__(self, browser, base_url, language):
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1280,1024')

        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        elif browser == "IE":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.base_url = base_url
        self.language = language

        self.session = SessionHelper(self)
        self.common_locators = Common()
        self.booking_widget_locators = BookingWidgetLocators()
        self.booking_widget = BookingWidget(self)
        self.main_page = MainPage(self)

    def destroy(self):
        self.wd.quit()
