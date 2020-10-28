from selenium import webdriver
from selenium.webdriver.common.by import By

class GetText():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element(By.ID, "openwindow")
        text_element = element.text
        print("text of Element is " + text_element)

        driver.quit()

ff = GetText()
ff.test()