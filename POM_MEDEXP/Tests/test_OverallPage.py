import time

from POM_MEDEXP.Pages.HomePage import HomePage
from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest

from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.DataFormPage import *
from POM_MEDEXP.Pages.ElectionsPage import *
from POM_MEDEXP.Pages.OverallPage import *


class Test_OverallPage(BaseTest):

    def test_new_selection(self):
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
        self.driver.find_element_by_css_selector("div:nth-child(2) > div:nth-child(1) > div > "
                                                 "div.ant-col.ant-form-item-control > div > div").click()
        formPage.select_date_range(TestData.BEGGIN_DATE, TestData.END_DATE)
        electionsPage.random_select_second_list()
        electionsPage.push_select_button()
        electionsPage.check_good_allert()
        proof = electionsPage.text_good_allert(TestData.TEXT_OF_ALLERT)

        assert proof == TestData.TEXT_OF_ALLERT


