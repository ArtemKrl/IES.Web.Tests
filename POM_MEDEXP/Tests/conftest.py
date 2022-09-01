import pytest
# import sys
# sys.path.append('C:/Users/Artem.Korol/IES.Web.Tests/POM_MEDEXP/')

from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.webdriver import WebDriver

from Config.capabilities import capabilities
from Config.config import selenoid_URL

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # web_driver = WebDriver()
        web_driver = webdriver.Remote(command_executor=selenoid_URL,desired_capabilities=capabilities)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
