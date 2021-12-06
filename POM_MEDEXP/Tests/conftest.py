import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.webdriver import WebDriver

from POM_MEDEXP.Config.capabilities import capabilities
from POM_MEDEXP.Config.config import selenoid_URL


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = WebDriver()
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()

# @pytest.fixture()
# def driver(request):
#     sel_driver = webdriver.Remote(
#         command_executor=selenoid_URL,
#         desired_capabilities=capabilities)
#     yield sel_driver
