from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class Screenshots:

    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web pag
        """
        fileName = str(round(time.time() * 1000)) + ".jpg"
        screenshotDirectory = "C:\\Users\\bunty\\Bunti_Naukri\\ScreenShot' + name +'.jpg"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot("C:\\Users\\bunty\\Bunti_Naukri\\ScreenShot' + name +'.jpg")
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshots()
ff.takeScreenshot()