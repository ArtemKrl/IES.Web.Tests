from selenium.webdriver.common.by import By

selenoid_URL = "http://192.168.20.191:4444/wd/hub"


class TestData:
    CHROME_EXECUTABLE_PATH = "/Users/Artem.Korol/Desktop/Selenium/geckodriver.exe"
    FIREFOX_EXECUTABLE_PATH = "/Users/Artem.Korol/Desktop/Selenium"

    BASE_URL = "http://ies-dev.test/"
    USER_NAME = "1"
    PASSWORD = "1"

    EXAMPLE_NUM_GOOD = "134.2"
    EXAMPLE_NUM_BAD = "666.66"

    LOGIN_PAGE_TITLE = 'Медэксперт'
    HOME_PAGE_TITLE = 'Медэксперт'
    DFS_TEXT = "Пояснения:"
    ERROR_TEXT = "Длина текста больше 5 символов"
    ATTRIBUTE_VALUE = "1"
    WRONG_DATA = "fsdfsd"
