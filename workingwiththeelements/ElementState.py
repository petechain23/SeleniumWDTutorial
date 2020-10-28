from selenium import webdriver

class ElementState():

    def isEnabled(self):
        baseUrl = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        e1 = driver.find_element_by_xpath("//form[@id='tsf']//div[@class='A8SBwf emcav sbfc']//div[@class='a4bIc']/input[@role='combobox']")
        e1State = e1.is_enabled() # True for enabled and False for disabled
        # print("E1 is Enabled? -> " + str(e1State))


        e1.send_keys("letskodeit")



e = ElementState()
e.isEnabled()