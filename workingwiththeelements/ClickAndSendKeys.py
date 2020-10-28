from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://letskodeit.teachable.com/"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #login button
        signup = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/ul/li[2]/a")
        signup.click()

        #User name
        user = driver.find_element(By.ID,"user_email")
        user.send_keys("username@letskodeit.com")

        #password
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("123456")

        time.sleep(5)
        user.clear()
        password.clear()

        time.sleep(5)
        driver.quit()

ff = ClickAndSendKeys()
ff.test()