import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Этот класс родитель всех страниц"""
"""Он содержит все общие методы и утилиты для всех страниц"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def execute_value(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute("value")

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_clear_area(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def check_element_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(by_locator, text))

    # def get_element_value(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return element.get_attribute('value')

    # driver.find_element_by_css_selector('.ant-input-number-input-wrap > input').get_attribute('value')
    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        #        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title))
        EC.visibility_of_element_located(title)
        return self.driver.title

    def get_home_page_title(self, title):
        #        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title))
        EC.visibility_of_element_located(title)
        return self.driver.title

    def do_double_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        actionChains = ActionChains(self.driver)
        actionChains.double_click(element).perform()

    def look_hidden_elem(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(element).perform()

<<<<<<< HEAD
    def wait_for_element_to_vanish(self, by_locator) -> bool:
        is_displayed = by_locator.is_displayed()
        start_time = self.get_current_time_in_mellis()
        time_interval_in_seconds = 5
        while is_displayed and not self.is_time_out(start_time, time_interval_in_seconds):
            is_displayed = by_locator.is_displayed()

        return not is_displayed
=======
>>>>>>> without_timeSleep
