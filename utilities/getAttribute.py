from selenium import webdriver
from selenium.webdriver.common.by import By

class GetAttribute():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element(By.ID, "name")
        value_element = element.get_attribute("type")
        print("Input of Element is: " + value_element)

        driver.quit()

ff = GetAttribute()
ff.test()