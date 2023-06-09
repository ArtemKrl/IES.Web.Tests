import time

import pytest
from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest
from POM_MEDEXP.Tests.conftest import init_driver

class Test_Login(BaseTest):

    def test_signup_link_clicable(self):
        self.loginPage = LoginPage(self.driver)
        time.sleep(1)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        time.sleep(1)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):

        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        check_in = self.loginPage.is_vitacore_logo_exist()
        assert check_in
