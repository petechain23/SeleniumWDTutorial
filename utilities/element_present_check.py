from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
import time

class ElementPresentCheck():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name",By.ID)
        print(str(elementResult1))

        elementResult2 = hw.isElementPresent('//input[@id="name"]', By.XPATH)
        print(str(elementResult2))

        driver.quit()

ff = ElementPresentCheck()
ff.test()