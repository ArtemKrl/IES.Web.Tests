import time
from BasePage import BasePage
from selenium.webdriver.common.by import By
import time
<<<<<<< HEAD
from array import *
from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.BasePage import BasePage
=======
from config import TestData
from BasePage import BasePage
>>>>>>> without_timeSleep
from selenium.webdriver.common.by import By
from test_base import BaseTest


class FormPage(BasePage):

    DFS_PAGE = (By.CSS_SELECTOR, "p:nth-child(1)")
    DROP_MENU_OPEN = (By.CSS_SELECTOR, "div:nth-child(3) > div:nth-child(1) > div > div.ant-col.ant-form-item-control > div > div > div")
    DROP_MENU_ITEM = (By.CSS_SELECTOR, "div.vc-sizer > div > div:nth-child(1) > div.vc-vt-sticky-left > label > span")
    CHECKBOX_CONTAINER = (By.CSS_SELECTOR, "label > span")
    CHECKBOX_FLAG = (By.CLASS_NAME, "ant-checkbox-checked")
    TEXT_FORM = (By.CSS_SELECTOR, "textarea")
    EMPTY_AREA = (By.CSS_SELECTOR, "div:nth-child(7)")
    ERROR_MESSAGE = (By.CLASS_NAME, "ant-form-item-explain-error")
    ARROW_UP = (By.CSS_SELECTOR, ".anticon-up > svg:nth-child(1)")
    ARROW_DOWN = (By.CSS_SELECTOR, ".ant-input-number-handler-down")
    VIEW_ARROW_COUNT = (By.CSS_SELECTOR, ".ant-input-number-input-wrap > input")
    ARROW_INPUT = (By.CSS_SELECTOR, ".ant-input-number-input-wrap > input")
    BIT_MENU = (By.CSS_SELECTOR, "div:nth-child(5) > div:nth-child(3) > div > div.ant-col.ant-form-item-control > div "
                                 "> div > div")
    BIT_ITEM_0 = (By.CSS_SELECTOR, ".ant-select-item-option-active")
    BIT_ITEM_1 = (By.CSS_SELECTOR, "div.ant-select-item:nth-child(2) > div:nth-child(1)")
    BIT_ITEM_3 = (By.CSS_SELECTOR, "div.ant-select-item:nth-child(4) > div:nth-child(1)")

    ITEM_IN_FORM_0 = (By.CSS_SELECTOR, "div.ant-select-selection-overflow-item:nth-child(1)")
    ITEM_IN_FORM_1 = (By.CSS_SELECTOR, "div.ant-select-selection-overflow-item:nth-child(2)")
    ITEM_IN_FORM_2 = (By.CSS_SELECTOR, "div.ant-select-selection-overflow-item:nth-child(3)")
    ITEM_IN_FORM_3 = (By.CSS_SELECTOR, "div.ant-select-selection-overflow-item:nth-child(4)")

    CLEAR_DATE = (By.CSS_SELECTOR, "span.ant-picker-clear:nth-child(6)")
    BEGIN_DATE = (By.CSS_SELECTOR, ".ant-picker-input-active > input")
    END_DATE = (By.CSS_SELECTOR, ".ant-picker-input-active > input")
    SELECT_DAY = (By.CSS_SELECTOR, ".ant-picker-cell-selected > div")
    SWIPE_LEFT = (By.CSS_SELECTOR, "div:nth-child(1) > div > div.ant-picker-header > "
                                   "button.ant-picker-header-super-prev-btn > span")
    SWIPE_LEFT_MIN = (By.CSS_SELECTOR, "div:nth-child(1) > div > div.ant-picker-header > "
                                       "button.ant-picker-header-prev-btn > span")
    SWIPE_RIGHT = (By.CSS_SELECTOR, "div:nth-child(2) > div > div.ant-picker-header > "
                                    "button.ant-picker-header-super-next-btn > span")
    MANUAL_FIRST_NUM = (By.CSS_SELECTOR, "div:nth-child(1) > div > div.ant-picker-body > table > tbody > "
                                         "tr:nth-child(1) > "
                                         "td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view")
    MANUAL_SECOND_NUM = (By.CSS_SELECTOR, ".ant-picker-cell-selected")

    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, ".ant-btn-sm > span:nth-child(2)")

    OPEN_DATEPICKER = (By.CSS_SELECTOR, ".ant-picker-input-active > input")

    SELECTOR_VALUE = (By.CSS_SELECTOR, ".ant-input-number-input-wrap > input")

    DATE_BEGIN_VALUE = (By.CSS_SELECTOR, ".ant-picker-range > div:nth-child(1) > input:nth-child(1)")
    DATE_END_VALUE = (By.CSS_SELECTOR, "div.ant-picker-input:nth-child(3) > input:nth-child(1)")

    ARROW_VALUE = (By.CSS_SELECTOR, ".ant-input-number-input-wrap > input")





    def __init__(self, driver):
        super().__init__(driver)
        self.driver.fullscreen_window()





    def check_drop_menu(self):
        self.do_click(self.DROP_MENU_OPEN)
        self.do_click(self.DROP_MENU_ITEM)

    def press_checkbox(self):
        return self.is_clickable(self.CHECKBOX_CONTAINER)

    def check_flag_checkbox(self):
        return self.is_visible(self.CHECKBOX_FLAG)

    def enter_textbox_good(self, example_num_good):
        self.do_clear_area(self.TEXT_FORM)
        self.do_send_keys(self.TEXT_FORM, example_num_good)
        self.do_click(self.EMPTY_AREA)

    def enter_textbox_bad(self, example_num_bad):
        self.do_clear_area(self.TEXT_FORM)
        self.do_send_keys(self.TEXT_FORM, example_num_bad)
        self.do_click(self.EMPTY_AREA)

    def check_num(self, text):
        return self.get_element_text(self.TEXT_FORM)

    def check_error_message(self, text):
        return self.get_element_text(self.ERROR_MESSAGE)

    def click_arrow_up(self):
        self.do_click(self.ARROW_UP)

    # def view_arrow_count(self, text):
    #     self.get_element_value(self.VIEW_ARROW_COUNT)

    def click_arrow_down(self):
        self.do_click(self.ARROW_DOWN)

    def enter_wrong_data(self, wrong_data):
        self.do_send_keys(self.ARROW_INPUT, wrong_data)
        self.do_click(self.EMPTY_AREA)

    def input_wrap(self):
        return self.execute_value(self.SELECTOR_VALUE)

    def elect_bit_item(self):
        time.sleep(1)
        self.do_click(self.BIT_MENU)
        self.do_click(self.BIT_ITEM_0)
        self.do_click(self.BIT_ITEM_1)
        self.do_click(self.BIT_ITEM_3)

    def check_bit_item(self):
<<<<<<< HEAD
        return self.is_visible(self.ITEM_IN_FORM_0), self.is_visible(self.ITEM_IN_FORM_1), self.is_visible(self.ITEM_IN_FORM_2), self.is_visible(self.ITEM_IN_FORM_3)

=======
        if self.is_visible(self.ITEM_IN_FORM_0):
            if self.is_visible(self.ITEM_IN_FORM_1):
                if self.is_visible(self.ITEM_IN_FORM_2):
                    return self.is_visible(self.ITEM_IN_FORM_3)
>>>>>>> without_timeSleep

    def push_btn_download(self):
        return self.is_clickable(self.DOWNLOAD_BUTTON)

    def select_date_range(self, beggin_date, end_date):
        time.sleep(1)
        self.do_click(self.OPEN_DATEPICKER)
        self.do_click(self.CLEAR_DATE)
        self.do_send_keys(self.BEGIN_DATE, beggin_date)
        self.do_click(self.SELECT_DAY)
        self.do_send_keys(self.END_DATE, end_date)
        self.do_click(self.SELECT_DAY)

    def select_date_range_manual(self):
        self.do_click(self.SWIPE_LEFT)
        self.do_click(self.SWIPE_LEFT)
        self.do_click(self.SWIPE_LEFT)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.SWIPE_LEFT_MIN)
        self.do_click(self.MANUAL_FIRST_NUM)
        self.do_click(self.MANUAL_SECOND_NUM)

    def getting_value_begin_date(self):
        return self.execute_value(self.DATE_BEGIN_VALUE)

    def getting_value_end_date(self):
        return self.execute_value(self.DATE_END_VALUE)

    def execute_arrow_value(self):
        return self.execute_value(self.ARROW_VALUE)






