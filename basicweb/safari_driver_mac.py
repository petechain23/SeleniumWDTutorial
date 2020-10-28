from selenium import webdriver
import time

class SafariDriver():

    def testMethod(self):
        driver = webdriver.Safari()
        driver.get("http:www.letskodeit.com")
        time.sleep(5)
        driver.quit()

driver = SafariDriver()
driver.testMethod()