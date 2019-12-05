from selenium.webdriver import Chrome
from Library import ConfigReader
from Base.InitiateDriver import test_BrowserDriver
# from ScreenShot import Shot
import configparser
from Pages import Jobs
import pytest
import unittest

from Pages.Jobs import test_ApplyJob
#from ScreenShot.teakS import test_Screenshot
from ScreenShot.teakS import take_page_sreenshot


class test_job():
    def test_srchjob(self):
        bd = test_BrowserDriver()
        self.driver = bd.test_startBrowser()
        #sc= test_Screenshot()
        #self.driver=sc.take_page_sreenshot("ghjk")
        log = test_ApplyJob
        # self.driver=log=Jobs.test_ApplyJob()
        self.driver=log.test_popmodal(self)
        self.driver = log.test_searchjob(self)
        # self.log.test_searchjob(driver)
        return test_job()


lookjob = test_job()
lookjob.test_srchjob()
