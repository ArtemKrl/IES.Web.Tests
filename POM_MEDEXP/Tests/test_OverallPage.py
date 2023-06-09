# import time
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from Pages.HomePage import HomePage
# from Pages.LoginPage import LoginPage
# from Tests.test_base import BaseTest
from POM_MEDEXP.Pages.BasePage import BasePage
from POM_MEDEXP.Pages.HomePage import HomePage
from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest

from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.DataFormPage import *
from POM_MEDEXP.Pages.ElectionsPage import *
from POM_MEDEXP.Pages.OverallPage import *
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Test_OverallPage(BaseTest):

    # def test_visibility_allert(self):
    #     try:
    #         self.loginPage = LoginPage(self.driver)
    #         homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #         homePage.follow_election()
    #         self.homePage = HomePage(self.driver)
    #         electionsPage = self.homePage.follow_election()
    #         electionsPage.elect_overall()
    #         electionsPage.create_new_election()
    #         electionsPage.fill_type_menu()
    #         time.sleep(1)
    #         electionsPage.fill_smo_menu()
    #         formPage = FormPage(self.driver)
    #         electionsPage.untried_checkbox()
    #         formPage.select_date_range(TestData.BEGIN_DATE, TestData.END_DATE)
    #         # electionsPage.random_select_second_list()
    #         electionsPage.tap_check_box()
    #         electionsPage.push_select_button()
    #         proof_1 = electionsPage.text_good_allert(TestData.TEXT_OF_ALLERT)
    #         electionsPage.check_good_allert()
    #         time.sleep(5)
    #         electionsPage.exp_checkbox()
    #         electionsPage.generate_req()
    #         electionsPage.breakdown_mo()
    #         electionsPage.go_generate_req()
    #         proof_2 = electionsPage.check_progress_bar()
    #         electionsPage.end_election()
    #
    #         proof_3 = electionsPage.allert_notice_check()
    #         assert proof_1 == TestData.TEXT_OF_ALLERT, proof_2
    #         assert proof_3
    #     finally:
    #         quit = self.homePage.quit_from_system()
    #         assert quit

    def test_empty_form(self):
        try:
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

        finally:
            quit = self.homePage.quit_from_system()
            assert quit



    def test_follow_bid_created(self):
        try:
            self.loginPage = LoginPage(self.driver)
            homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            homePage.follow_election()
            self.homePage = HomePage(self.driver)
            electionsPage = self.homePage.follow_election()
            electionsPage.elect_overall()
            electionsPage.create_new_election()
            electionsPage.follow_third_step()
            proof = electionsPage.check_error_allert(TestData.ATTENTION_TEXT_ERROR)
            assert proof == TestData.ATTENTION_TEXT_ERROR

        finally:
            quit = self.homePage.quit_from_system()
            assert quit


    def test_table_num_selection(self):
        try:
            self.loginPage = LoginPage(self.driver)
            homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            homePage.follow_election()
            self.homePage = HomePage(self.driver)
            electionsPage = self.homePage.follow_election()
            electionsPage.elect_overall()
            electionsPage.send_num_selection(TestData.NUM_SELECTION_3770)
            electionsPage.waiting_text_elem()

            search_data = electionsPage.execute_search_num(TestData.NUM_SELECTION_3770)
            assert TestData.NUM_SELECTION_3770 == search_data
            electionsPage.reset_set()
        finally:
            quit = self.homePage.quit_from_system()
            assert quit



    # def test_table_type_exp(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     homePage.follow_election()
    #     self.homePage = HomePage(self.driver)
    #     electionsPage = self.homePage.follow_election()
    #     electionsPage.elect_overall()
    #     time.sleep(3)
    #     electionsPage.choice_type_exp()
    #     time.sleep(1)
    #     search_data = electionsPage.execute_type_exp(TestData.VALUE_TYPE_EXP)
    #     check_clear = electionsPage.clear_type_exp()
    #     quit = self.homePage.quit_from_system()
    #
    #     assert TestData.VALUE_TYPE_EXP == search_data, check_clear
    #     assert quit

    def test_btn_point(self):
        try:
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
        finally:
            quit = self.homePage.quit_from_system()
            assert quit


    # def test_setting_сolumn(self):
    #     try:
    #         self.loginPage = LoginPage(self.driver)
    #         homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #         homePage.follow_election()
    #         self.homePage = HomePage(self.driver)
    #         electionsPage = self.homePage.follow_election()
    #         electionsPage.elect_overall()
    #         electionsPage.open_col_set()
    #         electionsPage.chch()

    #         electionsPage.multi_checked()
    #         proof = electionsPage.check_exp_column(TestData.EXP_TITLE)
    #         electionsPage.see_set_column()
    #         electionsPage.open_col_set()
    #         electionsPage.see_set_column()

    #         electionsPage.ne_rabotaet()
    #         electionsPage.multi_checked()
    #         time.sleep(2)
    #         electionsPage.reset_set()
    #
    #         electionsPage.ssc()
    #
    #
    #         electionsPage.multi_checked()
    #         assert proof == TestData.EXP_TITLE
    #
    #     finally:
    #         quit = self.homePage.quit_from_system()
    #         assert quit

    def test_checkbox_setting_сolumn(self):
        try:
            self.loginPage = LoginPage(self.driver)
            homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            homePage.follow_election()
            self.homePage = HomePage(self.driver)
            electionsPage = self.homePage.follow_election()
            electionsPage.elect_overall()
            electionsPage.open_col_set()
            # time.sleep(1)
            electionsPage.selective_checked()
            # time.sleep(2)
            electionsPage.selective_checked()
            # time.sleep(1)
        finally:
            quit = self.homePage.quit_from_system()
            assert quit




    def test_table_sorting_wrapper(self):
        try:
            self.loginPage = LoginPage(self.driver)
            homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            homePage.follow_election()
            self.homePage = HomePage(self.driver)
            electionsPage = self.homePage.follow_election()
            time.sleep(1)
            electionsPage.elect_overall()
            time.sleep(1)
            standard_sort = int(electionsPage.getting_standard_num())
            time.sleep(1)
            electionsPage.tap_sort_wrapper()
            time.sleep(1)
            down_sort = int(electionsPage.getting_small_num())
            time.sleep(1)
            electionsPage.tap_sort_wrapper()
            time.sleep(1)
            up_sort = int(electionsPage.getting_big_num())
            time.sleep(1)
            electionsPage.tap_sort_wrapper()
            time.sleep(1)
            standard_sort_2 = int(electionsPage.getting_standard_num())
            assert down_sort < up_sort
            # assert standard_sort == standard_sort_2

        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    def test_table_checkbox(self):
        try:
            self.loginPage = LoginPage(self.driver)
            homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            homePage.follow_election()
            self.homePage = HomePage(self.driver)
            electionsPage = self.homePage.follow_election()
            electionsPage.elect_overall()
            time.sleep(1)
            electionsPage.choice_checkbox()
            proof_1 = electionsPage.flag_box_check()

            proof_2 = electionsPage.check_cancel_box()
            electionsPage.cancel_box_table()
            assert proof_1
            assert proof_2
        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    def test_table_scroll(self):
        try:
            self.loginPage = LoginPage(self.driver)
            homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
            homePage.follow_election()
            self.homePage = HomePage(self.driver)
            electionsPage = self.homePage.follow_election()
            electionsPage.elect_overall()
            # time.sleep(1)
            time.sleep(1)
            electionsPage.check_element_text(electionsPage.MARK_ELEM, 'Выделено 0 элементов из')

            electionsPage.scroll_into_table()

            electionsPage.choice_checkbox()
            proof_1 = electionsPage.flag_box_check()
            time.sleep(2)
            electionsPage.choice_checkbox()
            time.sleep(2)
            electionsPage.choice_new_checkbox()

            electionsPage.check_cancel_box()
            # time.sleep(2)

            proof_2 = electionsPage.check_cancel_box()
            assert proof_1
            assert proof_2
        finally:
            quit = self.homePage.quit_from_system()
            assert quit

    # def test_create_cancel_election(self):
    #     try:
    #         self.loginPage = LoginPage(self.driver)
    #         homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #         homePage.follow_election()
    #         self.homePage = HomePage(self.driver)
    #         electionsPage = self.homePage.follow_election()
    #         electionsPage.elect_overall()
    #         time.sleep(1)
    #         electionsPage.send_num_selection(TestData.NUM_SELECTION_3770)
    #         electionsPage.waiting_text_elem()
    #         electionsPage.open_elect_3770()
    #         electionsPage.follow_two_step()
    #         electionsPage.open_atyashev()
    #         electionsPage.open_all_cases()
    #         proof_1 = electionsPage.choice_box_for_election(TestData.GOOD_ALLERT_TEXT_ELECT)
    #         electionsPage.close_allert()
    #         proof_2 = electionsPage.choice_box_for_cancel(TestData.BAD_ALLERT_TEXT_ELECT)
    #         assert proof_1 == TestData.GOOD_ALLERT_TEXT_ELECT
    #         assert proof_2 == TestData.BAD_ALLERT_TEXT_ELECT
    #     finally:
    #         quit = self.homePage.quit_from_system()
    #         assert quit

    # def test_fact_of_MEE(self):
    #     try:
    #         self.loginPage = LoginPage(self.driver)
    #         homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #         homePage.follow_election()
    #         self.homePage = HomePage(self.driver)
    #         electionsPage = self.homePage.follow_election()
    #         electionsPage.elect_overall()
    #         electionsPage.reset_set()
    #
    #         electionsPage.send_num_selection(TestData.NUM_SELECTION_1885)
    #         time.sleep(1)
    #
    #         electionsPage.open_elect_1885()
    #         electionsPage.follow_third_step()
    #         electionsPage.open_bid_1886()
    #         time.sleep(1)
    #         element = self.driver.find_element_by_css_selector(".vc-vt-row_green")
    #         if element.is_displayed():
    #             proof_1 = electionsPage.box_put_fact_MEE(TestData.ALLERT_FACT_CANCEL)
    #             electionsPage.close_allert()
    #             proof_2 = electionsPage.box_cancel_fact_MEE(TestData.ALLERT_FACT_PUT)
    #         else:
    #             proof_1 = electionsPage.box_put_fact_MEE(TestData.ALLERT_FACT_PUT)
    #             electionsPage.close_allert()
    #             time.sleep(1)
    #             proof_2 = electionsPage.box_cancel_fact_MEE(TestData.ALLERT_FACT_CANCEL)
    #         assert proof_1 == TestData.ALLERT_FACT_PUT
    #         assert proof_2 == TestData.ALLERT_FACT_CANCEL
    #         finally:
    #         quit = self.homePage.quit_from_system()
    #         assert quit


