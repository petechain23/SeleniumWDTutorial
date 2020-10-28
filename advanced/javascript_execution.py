from selenium import webdriver
from selenium.webdriver.common.by import By

class JavaScriptExecution():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(5)

        # driver.find_element(By.ID, "name").send_keys("test")
        element = driver.execute_script("return document.getElementById('name');")


ff = JavaScriptExecution()
ff.test()