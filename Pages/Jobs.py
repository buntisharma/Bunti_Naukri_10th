from lib2to3.pgen2 import driver

import selenium.webdriver
import self as self
from Library import ConfigReader

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class test_ApplyJob():
    def __init__(self,driver):
        self.driver = driver

    #def test_popmodal(self):
        #time.sleep(10)
        #self.driver.switch_to_alert()
        #time.sleep(5)
        #print(self.text)
        #self.driver.find_element_by_class_name(ConfigReader.test_PopUpmodal("Popup","Later")).click()

    def test_searchjob(self):
        time.sleep(10)
        self.driver.find_element_by_xpath(ConfigReader.test_searchlocal("Search", 'xpa')).click()
        #self.driver.find_element_by_class_name(ConfigReader.test_PopUpmodal("Popup", "Later")).click()
        self.driver.find_element_by_class_name(ConfigReader.test_searchlocal("Search", "Skill")).send_keys("python")
        self.driver.find_element_by_xpath(ConfigReader.test_searchlocal("Search", "Location")).send_keys("Chandigarh")
        self.driver.find_element_by_xpath(ConfigReader.test_searchlocal("Search", "Experience")).click()
        time.sleep(3)

