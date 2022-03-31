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
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.elect_DFS()
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        proof = formPage.press_checkbox()
        # proof = formPage.check_flag_checkbox()
        quit = self.homePage.quit_from_system()

        assert proof, quit


    def test_vc_TextBox_good(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        time.sleep(1)
        formPage.enter_textbox_good(TestData.EXAMPLE_NUM_GOOD)
        proof = formPage.check_num(TestData.EXAMPLE_NUM_GOOD)
        quit = self.homePage.quit_from_system()

        assert proof == TestData.EXAMPLE_NUM_GOOD, quit


    def test_vc_TextBox_bad(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        time.sleep(1)

        formPage.enter_textbox_bad(TestData.EXAMPLE_NUM_BAD)
        proof = formPage.check_error_message(TestData.ERROR_TEXT)
        quit = self.homePage.quit_from_system()

        assert proof == TestData.ERROR_TEXT, quit

    def test_vc_ArrowBox(self):
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
        proof = self.driver.find_element_by_css_selector('.ant-input-number-input-wrap > input').get_attribute('value')
        quit = self.homePage.quit_from_system()

        assert proof == "3466"
        assert quit

    def test_vc_ArrowBox_wrong_data(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.enter_wrong_data(TestData.WRONG_DATA)
        time.sleep(1)
        proof = formPage.input_wrap()
        quit = self.homePage.quit_from_system()

        assert proof == "3467"
        assert quit

    def test_BitChoice(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.elect_DFS()
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.elect_bit_item()
        proof = formPage.check_bit_item()
        quit = self.homePage.quit_from_system()

        assert proof, quit

    def test_datePicker(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        time.sleep(1)
        time.sleep(2)
        formPage.select_date_range(TestData.BEGGIN_DATE, TestData.END_DATE)
        proof_1 = self.driver.find_element_by_css_selector(".ant-picker-range > div:nth-child(1) > input:nth-child(1)").get_attribute("value")
        proof_2 = self.driver.find_element_by_css_selector("div.ant-picker-input:nth-child(3) > input:nth-child(1)").get_attribute("value")
        quit = self.homePage.quit_from_system()

        assert proof_1 == TestData.BEGGIN_DATE, proof_2 == TestData.END_DATE
        assert quit

    def test_datePicker_manual(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".ant-picker-input-active > input").click()
        time.sleep(2)
        formPage.select_date_range_manual()
        time.sleep(5)
        proof_1 = self.driver.find_element_by_css_selector(".ant-picker-range > div:nth-child(1) > input:nth-child(1)").get_attribute("value")
        proof_2 = self.driver.find_element_by_css_selector("div.ant-picker-input:nth-child(3) > input:nth-child(1)").get_attribute("value")
        quit = self.homePage.quit_from_system()

        assert proof_1 == TestData.BEGGIN_DATE, proof_2 == TestData.END_DATE_MANUAL
        assert quit
    def test_download_button(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        proof = formPage.push_btn_download()
        quit = self.homePage.quit_from_system()

        assert proof, quit

