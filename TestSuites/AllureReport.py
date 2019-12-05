from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import Main_Page
import pytest
from TestCases import test_log
#import HtmlTestRunner
from builtins import dir
import os
import time
import allure
class MyTestSuite():
#@pytest.fixture()
def test_runsuite(self):
        driver = InitiateDriver.teststartBrowser()
        nau=Main_Page.enter_creadential(self)
test_runsuite(self)
