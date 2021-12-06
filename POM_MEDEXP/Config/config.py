from selenium.webdriver.common.by import By

selenoid_URL = "http://192.168.20.191:4444/wd/hub"


class TestData:
    CHROME_EXECUTABLE_PATH = "/Users/Artem.Korol/Desktop/Selenium/geckodriver.exe"
    FIREFOX_EXECUTABLE_PATH = "/Users/Artem.Korol/Desktop/Selenium"

    BASE_URL = "http://ies-dev.test/"
    USER_NAME = "1"
    PASSWORD = "1"

    LOGIN_PAGE_TITLE = 'Медэксперт'
    HOME_PAGE_TITLE = 'Медэксперт'
