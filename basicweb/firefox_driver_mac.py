from selenium import webdriver
import time

class RunFFTests():

    def testMethod(self):
        #driver = webdriver.Firefox(executable_path="/Users/dattran/Documents/Virtualenv/PyCharm/workspace_python/driver/geckodriver")
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")
        time.sleep(5)
        driver.quit()

driver = RunFFTests()
driver.testMethod()