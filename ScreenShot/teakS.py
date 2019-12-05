from selenium.webdriver import Chrome

#class test_Screenshot:
def take_page_sreenshot(driver,name):

    driver.get_screenshot_as_file("C:\\Users\\bunty\\Bunti_Naukri\\ScreenShot' + name +'.jpg")

