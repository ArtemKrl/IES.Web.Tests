import time
import random

from POM_MEDEXP.Pages.DataFormPage import FormPage
from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class ElectionsPage(BasePage):

    OVERALL_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(1) > button')
    MTR_LPU_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(2) > button')
    HOSPITAL_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(3) > button')
    OUTGOING_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(4) > button')
    POLYCLINIC_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(5) > button')
    HOME_HOSPITAL = (By.CSS_SELECTOR, 'div:nth-child(6) > button')
    AMBULANCE_SELECTION = (By.CSS_SELECTOR, 'div:nth-child(7) > button')

    TITLE_PAGE = (By.CLASS_NAME, "ant-typography")
    HEADING_PAGE = (By.CLASS_NAME, "top-bar-caption")
    NEW_SELECTION = (By.CSS_SELECTOR, ".vt-vc-command-menu > div:nth-child(1) > div > button")

    TYPE_MENU_OPEN = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(1) > div > div.ant-col.ant-form-item-control > div > div")
    ITEM_TYPE_MENU = (By.CSS_SELECTOR, "div:nth-child(6) > div > div > div > div > div > div.vc-vt-grid-wrapper > "
                                       "div.sizer > div.vc-sizer > div > div:nth-child(1) > div:nth-child(2) > div")

    SMO_MENU_OPEN = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(2) > div > div.ant-col.ant-form-item-control "
                                      "> div > div")
    ITEM_SMO_MENU = (By.CSS_SELECTOR, ".ant-select-dropdown > div > div > div > div:nth-child(2) > div > "
                                      "div:nth-child(2) > div > div:nth-child(1)")

    FIRST_LIST_CHECKBOX = (By.CLASS_NAME, "ant-checkbox-input")
    SECOND_LIST_CHECKBOX = (By.CLASS_NAME, "ant-checkbox-input")

    SELECT_BUTTON = (By.CLASS_NAME, "ant-btn-primary")
    GOOD_ALLERT = (By.CLASS_NAME, "vitacore-ui-notification")
    ALLERT_TEXT = (By.CLASS_NAME, "ant-notification-notice-description")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.fullscreen_window()

    def check_text_title(self, text):
        return self.get_element_text(self.TITLE_PAGE)

    def check_text_heading(self, text):
        return self.get_element_text(self.HEADING_PAGE)


    def elect_overall(self):
        self.do_click(self.OVERALL_SELECTION)

    def elect_mtr_lpu(self):
        self.do_click(self.MTR_LPU_SELECTION)

    def elect_hospital(self):
        self.do_click(self.HOSPITAL_SELECTION)

    def elect_outgoing(self):
        self.do_click(self.OUTGOING_SELECTION)

    def elect_polyclinic(self):
        self.do_click(self.POLYCLINIC_SELECTION)

    def elect_home(self):
        self.do_click(self.HOME_HOSPITAL)

    def elect_ambulance(self):
        self.do_click(self.AMBULANCE_SELECTION)

    def create_new_election(self):
        self.do_click(self.NEW_SELECTION)

    def fill_type_menu(self):
        self.do_click(self.TYPE_MENU_OPEN)
        self.do_click(self.ITEM_TYPE_MENU)

    def fill_smo_menu(self):
        self.do_click(self.SMO_MENU_OPEN)
        self.do_click(self.ITEM_SMO_MENU)

    def select_items_first_list(self):
        self.do_click(self.FIRST_LIST_CHECKBOX)

    def random_select_second_list(self):
        first_list = self.driver.find_elements_by_class_name("ant-checkbox-input")
        choice_here_1 = first_list[6:7]
        random.choice(choice_here_1).click()  # random select one item
        choice_here_2 = first_list[8:9]
        random.choice(choice_here_2).click()  # random select one item
        time.sleep(1)
        second_list = self.driver.find_elements_by_class_name("ant-checkbox-input")
        choice_here_3 = second_list[11:12]
        random.choice(choice_here_3).click()  # random select one item
        choice_here_4 = second_list[13:15]
        random.choice(choice_here_4).click()  # random select one item

    def push_select_button(self):
        self.do_click(self.SELECT_BUTTON)

    def check_good_allert(self):
        self.is_visible(self.GOOD_ALLERT)

    def text_good_allert(self, text):
        return self.get_element_text(self.ALLERT_TEXT)
