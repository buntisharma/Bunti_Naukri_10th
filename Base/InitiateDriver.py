from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver

from Library import ConfigReader
Conn=ConfigReader
class test_BrowserDriver:
    def test_startBrowser(self):
        print("teststartBrowser method of BrowseDriver Class...")
        print("Browser from Config File ",ConfigReader.test_readConfigData('Details','Browser'))
        if ((ConfigReader.test_readConfigData('Details','Browser'))=="Chrome"):  #Condition to check browser
            path ="C:\\Users\\bunty\\Bunti_Naukri\\Driver\\chromedriver.exe"
            self.driver = Chrome(executable_path=path)
        elif((ConfigReader.test_readConfigData('Details','Browser'))=="firefox"):
            path = "C:\\Users\\bunti\\Downloads\\chromedriver_win32\\chromedriver.exe"
            self.driver = Chrome(executable_path=path)
        else:
            path = "E://chromedriver//chromedriver.exe"
            self.driver = Chrome(executable_path=path)

        #driver.get(ConfigReader.readConfigData('Details','Application_URL'))
        #To search the job directly
        self.driver.get(ConfigReader.test_readConfigData('Details','Application_URL2'))
        #driver.get("https://www.naukri.com/")
        self.driver.maximize_window()
        return self.driver
#teststartBrowser()

    def test_closebrowser(self):
        self.driver.close()
#"E:\\chromedriver.exe"