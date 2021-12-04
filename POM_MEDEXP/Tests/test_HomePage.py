from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
