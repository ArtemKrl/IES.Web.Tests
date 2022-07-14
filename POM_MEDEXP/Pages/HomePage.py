import time
from POM_MEDEXP.Pages.DataFormPage import FormPage
from POM_MEDEXP.Pages.ElectionsPage import ElectionsPage
from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class HomePage(BasePage):

    GENERAL_ADM = (By.CSS_SELECTOR, 'li:nth-child(2)')
    GENERAL_EXP = (By.CSS_SELECTOR, ".ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > "
                                    "div.ant-layout-sider-children > ul > li:nth-child(1) > "
                                    "span.anticon.ant-menu-item-icon > span")

    ADDITIONAL_ELECTION = (By.CSS_SELECTOR, '.ant-layout-sider-light.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > span.anticon.ant-menu-item-icon')
    ADDITIONAL_DFS = (By.CSS_SELECTOR, 'aside:nth-child(3) > div > ul > li:nth-child(2)')
    DFS_PAGE = (By.CSS_SELECTOR, "p:nth-child(1)")
    VITACORE_LOGO = (By.CSS_SELECTOR, ".vc-nr-logo > svg")

    QUIT_SYSTEM = (By.CSS_SELECTOR, ".anticon-logout.ant-menu-item-icon")
    LOGIN_PICTURE = (By.CSS_SELECTOR, "#login-page > div > div")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.fullscreen_window()




    def is_vitacore_logo_exist(self):
        return self.is_visible(self.VITACORE_LOGO)

    def elect_DFS(self):
        if self.is_visible(self.GENERAL_ADM):
            self.do_click(self.GENERAL_ADM)
        if self.is_visible(self.ADDITIONAL_DFS):
            self.do_click(self.ADDITIONAL_DFS)
        return FormPage(self.driver)

    def DFS_page_is_open(self, text):
        return self.get_element_text(self.DFS_PAGE)

    def follow_election(self):
        if self.is_visible(self.GENERAL_EXP):
            self.do_click(self.GENERAL_EXP)
        if self.is_visible(self.ADDITIONAL_ELECTION):
            self.do_click(self.ADDITIONAL_ELECTION)
        return ElectionsPage(self.driver)

    def login_page_is_visible(self):
        return self.is_visible(self.LOGIN_CONTAINER)

    def quit_from_system(self):
        self.do_click(self.QUIT_SYSTEM)
        return self.is_visible(self.LOGIN_PICTURE)





