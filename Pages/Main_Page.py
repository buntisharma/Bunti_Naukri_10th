#from lib2to3.pgen2 import driver
import selenium.webdriver
from Library import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class homepage:
    def __init__(self,obj):
        global driver
        driver=obj
        #to fetch the driver object we are creating the constructors here. To call the object of class homepage
        #we have to create the obj of class homepage

#To close the multiple opened pop-up windows
    def popwindow(self,driver):
        allwin=driver.window_handles
        mainWin =""
        for win in allwin:
            driver.switch_to.window(win)
            if (driver.current_url=="https://www.naukri.com"):
                    print("This is the main URL")
                    mainWin=win
                    driver.switch_to.window(mainWin)
            else:
                driver.close()
        driver.switch_to.window(mainWin)
    def main(self,driver):
        driver.switch_to.window(mainWin)











