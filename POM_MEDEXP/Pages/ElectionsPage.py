import time
import random

from POM_MEDEXP.Pages.DataFormPage import FormPage
from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from POM_MEDEXP.Config.config import TestData




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
    TWO_STEP_ELECT = (By.CSS_SELECTOR, "div:nth-child(2) > div > div.ant-steps-item-content > div")
    THREE_STEP_ELECT = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.ant-steps-item-content > div")

    TYPE_MENU_OPEN = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(1) > div > div.ant-col.ant-form-item-control > div > div")
    ITEM_TYPE_MENU = (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div")

    SMO_MENU_OPEN = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(2) > div > div.ant-col.ant-form-item-control "
                                      "> div > div")
    ITEM_SMO_MENU = (By.CSS_SELECTOR, ".ant-select-dropdown > div > div > div > div:nth-child(2) > div > "
                                      "div:nth-child(2) > div > div:nth-child(1)")

    FIRST_LIST_CHECKBOX = (By.CLASS_NAME, "ant-checkbox-input")
    SECOND_LIST_CHECKBOX = (By.CLASS_NAME, "ant-checkbox-input")

    SELECT_BUTTON = (By.CLASS_NAME, "ant-btn-primary")
    GOOD_ALLERT = (By.CLASS_NAME, "vitacore-ui-notification")
    ALLERT_TEXT = (By.CLASS_NAME, "ant-notification-notice-description")
    ERROR_TEXT = (By.CLASS_NAME, "ant-form-item-explain-error")
    TABLE_FORM_NUM_ELECTION = (By.CSS_SELECTOR, ".ant-input-number-input-wrap > input")
    SEARCH_ELECTION_NUM = (By.CSS_SELECTOR, "div.vc-vt-basic:nth-child(2) > div:nth-child(1)")
    UNTRIED_CHECKBOX = (By.CSS_SELECTOR, ".ant-checkbox-checked")
    EXP_CHECKBOX = (By.CSS_SELECTOR, "div:nth-child(1) > span.ant-tree-checkbox > span")
    GENERATE_REQ = (By.CSS_SELECTOR, ".ant-space-align-center > div:nth-child(2) > button")
    MO_CHECKBOX = (By.CSS_SELECTOR, "div:nth-child(2) > label > span.ant-checkbox")
    CREATE_REQ = (By.CSS_SELECTOR, ".ant-modal-footer > button.ant-btn.ant-btn-primary")
    END_ELECTION = (By.CSS_SELECTOR, ".ant-space-align-center > div:nth-child(1) > button")
    ACCEPT_END = (By.CSS_SELECTOR, ".ant-btn-primary.ant-btn-sm")
    GENERAL_INFO = (By.CSS_SELECTOR, ".vc-msf-heading")
    ITEM_SYS_DOTS = (By.CSS_SELECTOR, "div.vc-vt-row:nth-child(1) > div:nth-child(4) > button:nth-child(1) > span:nth-child(1)")
    ITEM_SYS_OPEN = (By.CSS_SELECTOR, ".vc-context-list > li:nth-child(1) > button:nth-child(1) > span:nth-child(2)")
    END_EVENTS = (By.CSS_SELECTOR, "div.vc-csf-filtersGroupItem:nth-child(1)")
    TYPE_EXP = (By.CSS_SELECTOR, ".sizer > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) "
                                 "> div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                 "div:nth-child(1)")
    MEE_ITEM = (By.CSS_SELECTOR, ".rc-virtual-list-holder > div > div > div:nth-child(2) > div")
    MEK_ITEM = (By.CSS_SELECTOR, ".rc-virtual-list-holder > div > div > div:nth-child(1) > div")
    VALUE_TABLE = (By.CSS_SELECTOR, "div.vc-vt-row:nth-child(1) > div:nth-child(3) > div:nth-child(1)")
    CLEAR_FORM = (By.CSS_SELECTOR, ".ant-select-clear")
    DROP_SET = (By.CSS_SELECTOR, ".drop-settings")
    RESET_ALL_SET = (By.CSS_SELECTOR, ".bold-item")
    YES_RESET = (By.CSS_SELECTOR, ".ant-btn-primary.ant-btn-sm")
    PROGRESS_BAR_ALLERT = (By.CSS_SELECTOR, ".progressBars")
    ERROR_ALLERT = (By.CLASS_NAME, "ant-notification-notice-message")
    BTN_POINT = (By.CSS_SELECTOR, ".vc-vt-row:nth-child(1) > div:nth-child(10) > button:nth-child(1)")
    EMPTY_CLICK = (By.CSS_SELECTOR, ".ant-layout-sider-light.ant-layout-sider-has-trigger > div.ant-layout-sider-children")
    BTN_DEL = (By.CSS_SELECTOR, "li:nth-child(2) > button:nth-child(1)")
    BTN_OPEN = (By.CSS_SELECTOR, "li:nth-child(1) > button:nth-child(1)")
    BTN_DEL_NOTIFICATION = (By.CSS_SELECTOR, ".ant-notification")
    COLUMN_SET = (By.CLASS_NAME, "column_settings")
    CHECKBOXES_COL_SET = (By.CSS_SELECTOR, ".ant-popover-inner > div > div > div > div > label > span > input")

    box_1 = (By.CSS_SELECTOR, ".ant-popover-inner > div > div > div:nth-child(2) > div:nth-child(1) > label > span")
    box_2 = (By.CSS_SELECTOR, "div > div > div > div:nth-child(2) > label > span")
    box_3 = (By.CSS_SELECTOR, "div > div > div > div:nth-child(3) > label > span")
    box_4 = (By.CSS_SELECTOR, "div > div > div > div:nth-child(4) > label > span")
    box_5 = (By.CSS_SELECTOR, "div > div > div > div:nth-child(5) > label > span")
    box_6 = (By.CSS_SELECTOR, "div > div > div > div:nth-child(6) > label > span")
    box_7 = (By.CSS_SELECTOR, "div > div > div > div:nth-child(7) > label > span")
    box_8 = (By.CSS_SELECTOR, "div > div > div > div:nth-child(8) > label > span")

    SAVE_SET = (By.CLASS_NAME, "vt-vc-header-menu-column-settings-btn-save")

    TYPE_EXP = (By.CSS_SELECTOR, ".sizer > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div > span")
    SORTING_WRAPPER_BTN = (By.CSS_SELECTOR, "div:nth-child(2) > div > div.vc-vt-sortingWrapper")
    SMALL_OR_BIG_NUM = (By.CSS_SELECTOR, ".vc-vt-row:nth-child(1) > div:nth-child(2) > div:nth-child(1)")



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
    def follow_two_step(self):
        self.do_click(self.TWO_STEP_ELECT)
    def follow_third_step(self):
        self.do_click(self.THREE_STEP_ELECT)

    def fill_type_menu(self):
        self.do_click(self.TYPE_MENU_OPEN)
        self.do_click(self.ITEM_TYPE_MENU)

    def fill_smo_menu(self):
        self.do_click(self.SMO_MENU_OPEN)
        self.do_click(self.ITEM_SMO_MENU)

    def select_items_first_list(self):
        self.do_click(self.FIRST_LIST_CHECKBOX)

    def check_error_allert(self, text):
       return self.get_element_text(self.ERROR_TEXT)

    def random_select_second_list(self):
        first_list = self.driver.find_elements_by_class_name("ant-checkbox-input")
        choice_here_1 = first_list[4:5]
        random.choice(choice_here_1).click()  # random select one item

        choice_here_2 = first_list[6:]
        random.choice(choice_here_2).click()  # random select one item
        choice_here_3 = first_list[7:8]
        random.choice(choice_here_3).click()  # random select one item
        time.sleep(1)
        second_list = self.driver.find_elements_by_class_name("ant-checkbox-input")
        choice_here_3 = second_list[10:12]
        random.choice(choice_here_3).click()  # random select one item
        choice_here_4 = second_list[13:14]
        random.choice(choice_here_4).click()  # random select one item

    def push_select_button(self):
        self.do_click(self.SELECT_BUTTON)

    def check_good_allert(self):
        self.is_visible(self.GOOD_ALLERT)

    def text_good_allert(self, text):
        return self.get_element_text(self.ALLERT_TEXT)


    def send_num_selection(self, num_selection):
        self.do_send_keys(self.TABLE_FORM_NUM_ELECTION, num_selection)

    def execute_search_num(self, text):
        return self.get_element_text(self.SEARCH_ELECTION_NUM)

    def untried_checkbox(self):
        self.do_click(self.UNTRIED_CHECKBOX)

    def exp_checkbox(self):
        self.do_click(self.EXP_CHECKBOX)

    def generate_req(self):
        self.do_click(self.GENERATE_REQ)

    def breakdown_mo(self):
        self.do_click(self.MO_CHECKBOX)

    def go_generate_req(self):
        self.do_click(self.CREATE_REQ)

    def end_election(self):
        self.do_click(self.END_ELECTION)
        self.do_click(self.ACCEPT_END)

    def choiсe_in_system(self):
        self.do_click(self.ITEM_SYS_DOTS)
        self.do_click(self.ITEM_SYS_OPEN)

    def follow_end_events(self):
        self.do_click(self.END_EVENTS)

    def choice_type_exp(self):
        self.do_click(self.TYPE_EXP)
        time.sleep(1)
        self.do_click(self.MEE_ITEM)
        self.do_click(self.MEK_ITEM)

    def execute_type_exp(self, text):
        return self.get_element_text(self.VALUE_TABLE)

    def clear_type_exp(self):
        self.do_click(self.TYPE_EXP)
        self.is_clickable(self.CLEAR_FORM)

    def reset_set(self):
        self.do_click(self.DROP_SET)
        self.do_click(self.RESET_ALL_SET)
        self.do_click(self.YES_RESET)

    def check_progress_bar(self):
        return self.is_visible(self.PROGRESS_BAR_ALLERT)

    def allert_notice_check(self):
        return self.is_visible(self.ERROR_ALLERT)

    def btn_point_del(self):
        self.do_click(self.BTN_POINT)
        self.do_click(self.BTN_DEL)
        return self.is_visible(self.BTN_DEL_NOTIFICATION)


    def btn_point_open(self):
        self.do_click(self.EMPTY_CLICK)

        self.do_click(self.BTN_POINT)
        self.do_click(self.BTN_OPEN)
        # return self.is_visible()

    def open_col_set(self):
        self.is_clickable(self.COLUMN_SET)
        self.do_click(self.COLUMN_SET)

    def multi_checked(self):
        self.do_click(self.box_2)
        self.do_click(self.box_3)
        self.do_click(self.box_4)
        self.do_click(self.box_5)
        self.do_click(self.box_6)
        self.do_click(self.box_7)
        self.do_click(self.box_8)

        self.do_click(self.SAVE_SET)

    def check_type_exp(self):
        self.is_visible(self.TYPE_EXP)

    def selective_checked(self):
        self.do_click(self.box_1)
        self.do_click(self.box_3)
        self.do_click(self.box_6)

    def tap_sort_wrapper(self):
        self.do_click(self.SORTING_WRAPPER_BTN)

    def getting_small_num(self):
        return self.get_element_text(self.SMALL_OR_BIG_NUM)

    def getting_big_num(self):
        return self.get_element_text(self.SMALL_OR_BIG_NUM)





