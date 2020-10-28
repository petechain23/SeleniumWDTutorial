from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ExplicitWaitDemo():
    def test(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        driver.find_element(By.ID)
        #Tab-Flight
        driver.quit()

ff = ExplicitWaitDemo()
ff.test()



