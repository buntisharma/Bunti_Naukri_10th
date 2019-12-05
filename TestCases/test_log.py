from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Library import ConfigReader
#from ScreenShot import Shot
import configparser
from Pages import Main_Page
import pytest
import unittest
class test():
    def test_Home():
        driver =InitiateDriver.teststartBrowser()
        log=Main_Page.homepage(driver)
        log.popwindow(driver)
        log.main(driver)
#Home()
#def testClosebrowser():
    #driver.close()
    #driver.quit()
#testClosebrowser()

