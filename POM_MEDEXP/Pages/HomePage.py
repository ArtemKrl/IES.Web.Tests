from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    GENERA_ADM = (By.CSS_SELECTOR, '.anticon-right-square.ant-menu-item-icon')
    ADDITIONAL_DFS = (By.CSS_SELECTOR, '.ant-layout-sider-light.ant-layout-sider-has-trigger > '
                                        'div.ant-layout-sider-children > ul > li:nth-child(3)')
    VITACORE_LOGO = (By.CSS_SELECTOR, ".NavRail_logo__2mva4 > svg")


    def __init__(self, driver):
        self().__init__(driver)

    def is_vitacore_logo_exist(self):
        return self.is_visible(self.VITACORE_LOGO)

    def elect_admin(self):
        if self.is_visible(self.GENERA_ADM):
            return self.do_click(self.GENERA_ADM)

    def elect_admin(self):
        if self.is_visible(self.ADDITIONAL_DFS):
            return self.do_click(self.ADDITIONAL_DFS)
