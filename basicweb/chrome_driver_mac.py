from selenium import webdriver
import time

class ChromeDriverMac():
    def testMethod(self):
        #driver = webdriver.Chrome(executable_path="/Users/dattran/Documents/Virtualenv/PyCharm/workspace_python/driver/chromedriver")
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")
        time.sleep(5)
        driver.quit()

driver = ChromeDriverMac()
driver.testMethod()