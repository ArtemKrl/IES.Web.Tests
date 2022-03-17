import time

from POM_MEDEXP.Pages.HomePage import HomePage
from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest

from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.DataFormPage import *
from POM_MEDEXP.Pages.ElectionsPage import *
from POM_MEDEXP.Pages.OverallPage import *


class Test_OverallPage(BaseTest):

    # def test_new_selection(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     homePage.follow_election()
    #     self.homePage = HomePage(self.driver)
    #     electionsPage = self.homePage.follow_election()
    #     electionsPage.elect_overall()
    #     electionsPage.create_new_election()
    #     electionsPage.fill_type_menu()
    #     electionsPage.fill_smo_menu()
    #     formPage = FormPage(self.driver)
    #     electionsPage.untried_checkbox()
    #
    #     self.driver.find_element_by_css_selector("div:nth-child(2) > div:nth-child(1) > div > "
    #                                              "div.ant-col.ant-form-item-control > div > div").click()
    #     formPage.select_date_range(TestData.BEGGIN_DATE, TestData.END_DATE)
    #
    #     electionsPage.random_select_second_list()
    #     electionsPage.push_select_button()
    #     proof = electionsPage.text_good_allert(TestData.TEXT_OF_ALLERT)
    #     electionsPage.check_good_allert()
    #     # electionsPage.choiсe_in_system()
    #
    #     electionsPage.exp_checkbox()
    #     electionsPage.generate_req()
    #     electionsPage.breakdown_mo()
    #     electionsPage.go_generate_req()
    #     electionsPage.end_election()
    #     time.sleep(100)
    #
    #     assert proof == TestData.TEXT_OF_ALLERT

    def test_empty_form(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.create_new_election()
        electionsPage.follow_two_step()

        proof = electionsPage.check_error_allert(TestData.ATTENTION_TEXT_ERROR)
        assert proof == TestData.ATTENTION_TEXT_ERROR

    def test_follow_bid_created(self):
        self.loginPage = LoginPage(self.driver)
        # homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.create_new_election()
        electionsPage.follow_third_step()
        proof = electionsPage.check_error_allert(TestData.ATTENTION_TEXT_ERROR)
        assert proof == TestData.ATTENTION_TEXT_ERROR

    def test_table_num_selection(self):
        self.loginPage = LoginPage(self.driver)
        # homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.send_num_selection(TestData.NUM_SELECTION)
        time.sleep(1)
        search_data = electionsPage.execute_search_num(TestData.NUM_SELECTION)
        assert TestData.NUM_SELECTION == search_data
        electionsPage.reset_set()

    def test_table_type_exp(self):
        self.loginPage = LoginPage(self.driver)
        # homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.choice_type_exp()
        time.sleep(1)
        search_data = electionsPage.execute_type_exp(TestData.VALUE_TYPE_EXP)
        check_clear = electionsPage.clear_type_exp()

        assert TestData.VALUE_TYPE_EXP == search_data, check_clear




