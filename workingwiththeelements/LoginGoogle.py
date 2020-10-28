from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "http://localhost:8080/login"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #name page
        title = driver.title
        print(title)

        #User name
        user = driver.find_element(By.XPATH,"//input[@id='j_username']")
        user.send_keys("Admin")

        #password
        password = driver.find_element(By.XPATH, "//div[@role='main']//form[@name='login']//input[@name='j_password']")
        password.send_keys("123")

        #current page
        currentpage = driver.current_url
        print(currentpage)

        # name page
        title = driver.title
        print(title)

        # login button
        login = driver.find_element(By.XPATH, "/html//div[@role='main']//form[@name='login']//input[@name='Submit']")
        login.click()
        time.sleep(3)

        # logout button
        logout = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/a[2]/span")
        logout.click()

        time.sleep(3)
        driver.quit()

ff = ClickAndSendKeys()
ff.test()