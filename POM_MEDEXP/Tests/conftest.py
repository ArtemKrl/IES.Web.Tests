import pytest
from selenium import webdriver
from POM_MEDEXP.Config.config import TestData
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        #web_driver = WebDriver()
        web_driver = webdriver.Remote(command_executor=selenoid_URL,desired_capabilities=capabilities)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
