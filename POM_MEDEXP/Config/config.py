from selenium.webdriver.common.by import By

selenoid_URL = "http://selenoid:4444/wd/hub"


class TestData:
    CHROME_EXECUTABLE_PATH = "/Users/Artem.Korol/Desktop/Selenium/geckodriver.exe"
    FIREFOX_EXECUTABLE_PATH = "/Users/Artem.Korol/Desktop/Selenium"

#    BASE_URL = "http://ies-rc.test/"
    BASE_URL = "http://web:80/"
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

    BEGIN_DATE = "01.01.2018"
    END_DATE = "01.01.2022"

    END_DATE_MANUAL = "20.01.2022"
    ELECTIONS_PAGE_TITLE = "Выберите отбор"

    OVERALL_HEADING = "Отборы / Общий отбор"
    MTR_LPU_HEADING = "Отборы / Отбор по счетам МТР от ЛПУ"
    HOSPITAL_HEADING = "Отборы / Отборы по стационару"
    OUTGOING_HEADING = "Отборы / Отбор по исходящим счетам"
    POLYCLINIC_HEADING = "Отборы / Отборы по поликлинике"
    HOME_HOSPITAL_HEADING = "Отборы / Стационар на дому"
    AMBULANCE_HEADING = "Отборы / Отборы по скорой помощи"

    TEXT_OF_ALLERT = "Данные формы сохранены"