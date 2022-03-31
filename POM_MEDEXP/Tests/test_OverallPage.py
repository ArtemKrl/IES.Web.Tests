import time

from POM_MEDEXP.Pages.HomePage import HomePage
from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest

from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.DataFormPage import *
from POM_MEDEXP.Pages.ElectionsPage import *
from POM_MEDEXP.Pages.OverallPage import *


class Test_OverallPage(BaseTest):

    def test_visibility_allert(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.create_new_election()
        electionsPage.fill_type_menu()
        electionsPage.fill_smo_menu()
        formPage = FormPage(self.driver)
        electionsPage.untried_checkbox()
        formPage.select_date_range(TestData.BEGGIN_DATE, TestData.END_DATE)
        electionsPage.random_select_second_list()
        electionsPage.push_select_button()
        proof_1 = electionsPage.text_good_allert(TestData.TEXT_OF_ALLERT)
        electionsPage.check_good_allert()
        electionsPage.exp_checkbox()
        electionsPage.generate_req()
        electionsPage.breakdown_mo()
        electionsPage.go_generate_req()
        proof_2 = electionsPage.check_progress_bar()
        electionsPage.end_election()

        proof_3 = electionsPage.allert_notice_check()
        quit = self.homePage.quit_from_system()

        assert proof_1 == TestData.TEXT_OF_ALLERT, proof_2
        assert proof_3, quit

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
        quit = self.homePage.quit_from_system()

        assert proof == TestData.ATTENTION_TEXT_ERROR
        assert quit



    def test_follow_bid_created(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.create_new_election()
        electionsPage.follow_third_step()
        proof = electionsPage.check_error_allert(TestData.ATTENTION_TEXT_ERROR)
        quit = self.homePage.quit_from_system()

        assert proof == TestData.ATTENTION_TEXT_ERROR
        assert quit


    def test_table_num_selection(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.send_num_selection(TestData.NUM_SELECTION)
        time.sleep(1)
        search_data = electionsPage.execute_search_num(TestData.NUM_SELECTION)
        assert TestData.NUM_SELECTION == search_data
        electionsPage.reset_set()
        quit = self.homePage.quit_from_system()
        assert quit



    def test_table_type_exp(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        electionsPage.choice_type_exp()
        time.sleep(1)
        search_data = electionsPage.execute_type_exp(TestData.VALUE_TYPE_EXP)
        check_clear = electionsPage.clear_type_exp()
        quit = self.homePage.quit_from_system()

        assert TestData.VALUE_TYPE_EXP == search_data, check_clear
        assert quit

    def test_btn_point(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        time.sleep(1)
        proof_1 = electionsPage.btn_point_del()
        electionsPage.btn_point_open()
        proof_2 = electionsPage.check_text_heading(TestData.OVERALL_HEADING)
        assert proof_1, proof_2
        quit = self.homePage.quit_from_system()

        assert quit






