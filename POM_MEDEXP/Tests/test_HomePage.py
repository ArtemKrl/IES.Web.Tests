import time

from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest

from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.HomePage import HomePage


class Test_Home(BaseTest):

    # def test_home_page_logo(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     self.homePage = HomePage(self.driver)
    #     check_in = homePage.is_vitacore_logo_exist()
    #     time.sleep(1)
    #     quit = self.homePage.quit_from_system()

    #     assert check_in, quit


    # def test_follow_to_DFS(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     self.homePage = HomePage(self.driver)
    #     self.homePage.elect_DFS()
    #     page = self.homePage.DFS_page_is_open(TestData.DFS_TEXT)
    #     quit = self.homePage.quit_from_system()
    #     assert page == TestData.DFS_TEXT, quit




