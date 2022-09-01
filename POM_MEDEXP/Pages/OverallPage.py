# import time
# from Pages.DataFormPage import FormPage
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC




class OverallPage(BasePage):

    TITLE_PAGE = (By.CLASS_NAME, "ant-typography")
    HEADING_PAGE = (By.CLASS_NAME, "top-bar-caption")
    TABLE_FORM_NUM_ELECTION = (By.CLASS_NAME, "ant-input-number-input-wrap")




    def __init__(self, driver):
        super().__init__(driver)
        self.driver.fullscreen_window()

    def check_text_title(self, text):
        return self.get_element_text(self.TITLE_PAGE)

    def check_text_heading(self, text):
        return self.get_element_text(self.HEADING_PAGE)

    def table_form_num_on(self):
        self.do_click(self.TABLE_FORM_NUM_ELECTION)
