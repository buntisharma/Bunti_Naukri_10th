from selenium.webdriver import Chrome
path="F:\\chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.phptravels.net/")
driver.maximize_window()
#driver.find_element_by_class_name("icon_set_1_icon-70 go-right").click()
#driver.find_elements_by_css_selector("#li_myaccount").click()
driver.implicitly_wait(5)
#driver.find_element_by_xpath("//text()[contains(.,'My Account')]/ancestor::a[1]").click()
#driver.find_element_by_class_name("lightcaret mt-2 go-left").click()
#driver.find_element_by_link_text("Offers").click()
driver.find_elements_by_css_selector('li#li_myaccount').click()
#("#li_myaccount")