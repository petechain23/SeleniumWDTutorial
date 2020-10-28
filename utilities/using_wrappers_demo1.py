from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
import time

class UsingWrappers():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        hw = HandyWrappers(driver)
        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']",locatorType='xpath')
        textField2.clear()

        driver.quit()

ff = UsingWrappers()
ff.test()