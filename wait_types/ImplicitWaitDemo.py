from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        # implicitly wait with 10 seconds
        # e.g .5 => 5 miliseconds
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()

        user_login = driver.find_element(By.ID, 'user_email')
        user_login.send_keys('test@letskodeit.com')

        pass_input = driver.find_element(By.ID, "user_password")
        pass_input.send_keys('123456')

        # Explicit wait with 2 seconds
        time.sleep(2)
        user_login.clear()
        pass_input.clear()

        driver.quit()

ff = ImplicitWaitDemo()
ff.test()



