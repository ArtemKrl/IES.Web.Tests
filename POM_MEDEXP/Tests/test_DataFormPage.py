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
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        time.sleep(1)
        formPage.enter_textbox_good(TestData.EXAMPLE_NUM_GOOD)
        proof = formPage.check_num(TestData.EXAMPLE_NUM_GOOD)
        assert proof == TestData.EXAMPLE_NUM_GOOD


    def test_vc_TextBox_bad(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.enter_textbox_bad(TestData.EXAMPLE_NUM_BAD)
        proof = formPage.check_error_message(TestData.ERROR_TEXT)
        assert proof == TestData.ERROR_TEXT

    def test_vc_ArrowBox(self):
        self.loginPage = LoginPage(self.driver)
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
        assert proof == "2"

    def test_vc_ArrowBox_wrong_data(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.enter_wrong_data(TestData.WRONG_DATA)
        proof = self.driver.find_element_by_css_selector('.ant-input-number-input-wrap > input').get_attribute(
                 'value')
        assert proof == "3"

    def test_BitChoice(self):
        self.loginPage = LoginPage(self.driver)
        # homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.elect_DFS()
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        formPage.elect_bit_item()
        proof = formPage.check_bit_item()
        assert proof

    def test_datePicker(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        time.sleep(1)
        self.driver.find_element_by_css_selector("div:nth-child(5) > div:nth-child(1) > div > "
                                                 "div.ant-col.ant-form-item-control > div > div").click()
        time.sleep(1)
        formPage.select_date_range(TestData.BEGGIN_DATE, TestData.END_DATE)
        proof_1 = self.driver.find_element_by_css_selector(".ant-picker-range > div:nth-child(1) > input:nth-child(1)").get_attribute("value")
        proof_2 = self.driver.find_element_by_css_selector("div.ant-picker-input:nth-child(3) > input:nth-child(1)").get_attribute("value")
        assert proof_1 == TestData.BEGGIN_DATE, proof_2 == TestData.END_DATE

    def test_download_button(self):
        self.loginPage = LoginPage(self.driver)
        # homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.elect_DFS()
        self.homePage = HomePage(self.driver)
        formPage = self.homePage.elect_DFS()
        proof = formPage.push_btn_download()
        assert proof

