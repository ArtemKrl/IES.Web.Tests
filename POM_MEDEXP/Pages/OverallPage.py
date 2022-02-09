import time
from POM_MEDEXP.Pages.DataFormPage import FormPage
from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class OverallPage(BasePage):

    OVERALL_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(1) > button')
    MTR_LPU_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(2) > button')
    HOSPITAL_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(3) > button')
    OUTGOING_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(4) > button')
    POLYCLINIC_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(5) > button')
    HOME_HOSPITAL = (By.CSS_SELECTOR, 'div:nth-child(6) > button')
    AMBULANCE_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(7) > button')

    TITLE_PAGE = (By.CLASS_NAME, "ant-typography")
    HEADING_PAGE = (By.CLASS_NAME, "top-bar-caption")




    def __init__(self, driver):
        super().__init__(driver)
        self.driver.fullscreen_window()

    def check_text_title(self, text):
        return self.get_element_text(self.TITLE_PAGE)

    def check_text_heading(self, text):
        return self.get_element_text(self.HEADING_PAGE)
