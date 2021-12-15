import time
from POM_MEDEXP.Pages.DataFormPage import FormPage
from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class HomePage(BasePage):

    GENERAL_ADM = (By.CSS_SELECTOR, '.anticon-right-square.ant-menu-item-icon')
    ADDITIONAL_DFS = (By.CSS_SELECTOR, '.ant-menu-light > li:nth-child(2) > span:nth-child(1)')
    DFS_PAGE = (By.CSS_SELECTOR, "p:nth-child(1)")
    VITACORE_LOGO = (By.CSS_SELECTOR, ".NavRail_logo__2mva4 > svg")


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



