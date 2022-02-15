import pytest
from selenium.webdriver.common.by import By
import time
from POM_MEDEXP.Config.config import selenoid_URL
from selenium import webdriver
from POM_MEDEXP.Config.capabilities import capabilities
import pytest
from POM_MEDEXP.Pages.DataFormPage import FormPage
from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.BasePage import BasePage
from POM_MEDEXP.Pages.HomePage import HomePage


class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "#normal_login_username")
    PASSWORD = (By.CSS_SELECTOR, "#normal_login_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    SIGNUP_LINK = (By.CSS_SELECTOR, "button > span")
    VITACORE_LOGO = (By.CSS_SELECTOR, ".vc-nr-logo > svg")

    """Конструктор класса страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.fullscreen_window()



    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_clickable(self.SIGNUP_LINK)

    def is_vitacore_logo_exist(self):
        return self.is_visible(self.VITACORE_LOGO)

    """это используется для входа в аккаунт"""

    def do_login(self, username, password):
        self.driver.fullscreen_window()
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
