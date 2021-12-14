import time

from POM_MEDEXP.Pages.HomePage import HomePage
from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest

from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.DataFormPage import *


class Test_DataForm(BaseTest):

    # def test_vc_DropDown_menu(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     # homePage.elect_DFS()
    #     self.homePage = HomePage(self.driver)
    #     formPage = self.homePage.elect_DFS()
    #     formPage.check_drop_menu()
    #     time.sleep(15)

    def test_vc_CheckBox(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.elect_DFS()
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.press_checkbox()
        proof = formPage.check_flag_checkbox()
        assert proof

    def test_vc_TextBox_good(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.elect_DFS()
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.enter_textbox_good(TestData.EXAMPLE_NUM_GOOD)
        proof = formPage.check_num(TestData.EXAMPLE_NUM_GOOD)
        assert proof == TestData.EXAMPLE_NUM_GOOD

    def test_vc_TextBox_bad(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.elect_DFS()
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.enter_textbox_bad(TestData.EXAMPLE_NUM_BAD)
        proof = formPage.check_error_message(TestData.ERROR_TEXT)
        assert proof == TestData.ERROR_TEXT

