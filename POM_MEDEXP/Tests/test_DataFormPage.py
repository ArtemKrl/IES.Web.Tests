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
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            # homePage.elect_DFS()
            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            proof = formPage.press_checkbox()
            assert proof
        finally:
            quit = self.homePage.quit_from_system()
            assert quit


    def test_vc_TextBox_good(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            time.sleep(1)
            formPage.enter_textbox_good(TestData.EXAMPLE_NUM_GOOD)
            proof = formPage.check_num(TestData.EXAMPLE_NUM_GOOD)
            assert proof == TestData.EXAMPLE_NUM_GOOD
        finally:
            quit = self.homePage.quit_from_system()
            assert quit


    def test_vc_TextBox_bad(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            time.sleep(1)

            formPage.enter_textbox_bad(TestData.EXAMPLE_NUM_BAD)
            proof = formPage.check_error_message(TestData.ERROR_TEXT)
            assert proof == TestData.ERROR_TEXT
        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    def test_vc_ArrowBox(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            time.sleep(1)
            self.driver.find_element_by_css_selector(".ant-input-number").click()
            formPage.click_arrow_up()
            formPage.click_arrow_up()
            formPage.click_arrow_down()
            formPage.click_arrow_down()
            formPage.click_arrow_down()
            proof = formPage.execute_arrow_value()
            assert proof == "33"

        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    def test_vc_ArrowBox_wrong_data(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            formPage.enter_wrong_data(TestData.WRONG_DATA)
            time.sleep(1)
            proof = formPage.input_wrap()
            assert proof == "34"
        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    def test_BitChoice(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            # homePage.elect_DFS()
            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            formPage.elect_bit_item()
            proof = formPage.check_bit_item()
            assert proof == True
        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    def test_datePicker(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            time.sleep(1)
            time.sleep(2)
            formPage.select_date_range(TestData.BEGIN_DATE, TestData.END_DATE)
            proof_1 = formPage.getting_value_begin_date()
            proof_2 = formPage.getting_value_end_date()
            assert proof_1 == TestData.BEGIN_DATE, proof_2 == TestData.END_DATE

        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    def test_datePicker_manual(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            time.sleep(1)
            self.driver.find_element_by_css_selector(".ant-picker-input-active > input").click()
            time.sleep(2)
            formPage.select_date_range_manual()
            time.sleep(2)
            proof_1 = formPage.getting_value_begin_date()
            proof_2 = formPage.getting_value_end_date()
            assert proof_1 == TestData.BEGIN_DATE, proof_2 == TestData.END_DATE_MANUAL
        finally:
            quit = self.homePage.quit_from_system()
            assert quit


    def test_download_button(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            self.homePage = HomePage(self.driver)
            formPage = self.homePage.elect_DFS()
            proof = formPage.push_btn_download()
            assert proof
        finally:
            quit = self.homePage.quit_from_system()
            assert quit

