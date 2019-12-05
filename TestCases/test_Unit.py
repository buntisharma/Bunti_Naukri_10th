from selenium.webdriver import Chrome
from Library import ConfigReader
from Base.InitiateDriver import test_BrowserDriver
#from ScreenShot import Shot
import configparser
from Pages import Jobs
import pytest
import unittest
from Pages import Main_Page
class TestPyTestClass(unittest.Main_Page):
    def test_srchjob(self):
        bd = test_BrowserDriver()
        self.driver = bd.test_startBrowser()
        log = Jobs.test_ApplyJob(self.driver)
        log.test_searchjob(self.driver)