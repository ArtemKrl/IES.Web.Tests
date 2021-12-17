import time
from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from POM_MEDEXP.Config.config import TestData
from POM_MEDEXP.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from POM_MEDEXP.Tests.test_base import BaseTest


class FormPage(BasePage):

    DFS_PAGE = (By.CSS_SELECTOR, "p:nth-child(1)")
    DROP_MENU_OPEN = (By.CSS_SELECTOR, "div:nth-child(3) > div:nth-child(1) > div > div.ant-col.ant-form-item-control > div > div > div")
    DROP_MENU_ITEM = (By.CSS_SELECTOR, "div.vc-sizer > div > div:nth-child(1) > div.vc-vt-sticky-left > label > span")
    CHECKBOX_CONTAINER = (By.CSS_SELECTOR, "label > span")
    CHECKBOX_FLAG = (By.CLASS_NAME, "ant-checkbox-checked")
    TEXT_FORM = (By.CSS_SELECTOR, "textarea")
    EMPTY_AREA = (By.CSS_SELECTOR, "div:nth-child(7)")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".ant-form-item-explain-error > div")
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
    BEGGIN_DATE = (By.CSS_SELECTOR, ".ant-picker-input-active > input")
    END_DATE = (By.CSS_SELECTOR, ".ant-picker-input-active > input")
    SELECT_DAY = (By.CSS_SELECTOR, ".ant-picker-cell-selected > div")

    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, ".ant-btn-sm > span:nth-child(2)")






    def __init__(self, driver):
        super().__init__(driver)
        self.driver.fullscreen_window()




    def check_drop_menu(self):
        self.do_click(self.DROP_MENU_OPEN)
        self.do_click(self.DROP_MENU_ITEM)

    def press_checkbox(self):
        self.do_click(self.CHECKBOX_CONTAINER)

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

    def elect_bit_item(self):
        self.do_click(self.BIT_MENU)
        self.do_click(self.BIT_ITEM_0)
        self.do_click(self.BIT_ITEM_1)
        self.do_click(self.BIT_ITEM_3)

    def check_bit_item(self):
        return self.is_visible(self.ITEM_IN_FORM_0)
        return self.is_visible(self.ITEM_IN_FORM_1)
        return self.is_visible(self.ITEM_IN_FORM_2)
        return self.is_visible(self.ITEM_IN_FORM_3)

    def push_btn_download(self):
        return self.is_clickable(self.DOWNLOAD_BUTTON)

    def select_date_range(self, beggin_date, end_date):
        self.do_click(self.CLEAR_DATE)
        self.do_send_keys(self.BEGGIN_DATE, beggin_date)
        self.do_click(self.SELECT_DAY)
        self.do_send_keys(self.END_DATE, end_date)
        self.do_click(self.SELECT_DAY)



