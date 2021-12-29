import time

from POM_MEDEXP.Pages import ElectionsPage
from POM_MEDEXP.Pages.HomePage import HomePage
from POM_MEDEXP.Pages.LoginPage import LoginPage
from POM_MEDEXP.Tests.test_base import BaseTest

from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.DataFormPage import *


class Test_ElectionPage(BaseTest):

    def test_check_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.check_text_title(TestData.ELECTIONS_PAGE_TITLE)
        proof = electionsPage.check_text_title(TestData.ELECTIONS_PAGE_TITLE)
        assert proof == TestData.ELECTIONS_PAGE_TITLE

    def test_elect_overall(self):
        self.loginPage = LoginPage(self.driver)
        # homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # homePage.follow_election()
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_overall()
        proof = electionsPage.check_text_heading(TestData.OVERALL_HEADING)
        assert proof == TestData.OVERALL_HEADING

    def test_elect_myr_lpu(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_mtr_lpu()
        proof = electionsPage.check_text_heading(TestData.MTR_LPU_HEADING)
        assert proof == TestData.MTR_LPU_HEADING

    def test_elect_hospital(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_hospital()
        proof = electionsPage.check_text_heading(TestData.HOSPITAL_HEADING)
        assert proof == TestData.HOSPITAL_HEADING

    def test_elect_outgoing(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_outgoing()
        proof = electionsPage.check_text_heading(TestData.OUTGOING_HEADING)
        assert proof == TestData.OUTGOING_HEADING

    def test_elect_polyclinic(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_polyclinic()
        proof = electionsPage.check_text_heading(TestData.POLYCLINIC_HEADING)
        assert proof == TestData.POLYCLINIC_HEADING

    def test_elect_home(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_home()
        proof = electionsPage.check_text_heading(TestData.HOME_HOSPITAL_HEADING)
        assert proof == TestData.HOME_HOSPITAL_HEADING

    def test_elect_ambulance(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        electionsPage = self.homePage.follow_election()
        electionsPage.elect_ambulance()
        proof = electionsPage.check_text_heading(TestData.AMBULANCE_HEADING)
        assert proof == TestData.AMBULANCE_HEADING