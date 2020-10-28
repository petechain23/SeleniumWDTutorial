from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToAlert():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.title

        # input some text to search box
        driver.find_element_by_id("name").send_keys("Test Alert...")
        time.sleep(1)

        # press Alert button then popup to be showed
        driver.find_element_by_id("alertbtn").click()
        time.sleep(1)

        # Handle Alert popup by Javascript
        alert = driver.switch_to.alert
        # Accept
        alert.accept()
        time.sleep(2)

        # input some text to search box
        driver.find_element_by_id("name").send_keys("Test Accept Alert...")
        time.sleep(1)

        # press Confirm button then popup to be showed
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(1)

        # Confirm
        alert2 = driver.switch_to.alert
        alert2.accept()
        time.sleep(2)

        # input some text to search box
        driver.find_element_by_id("name").send_keys("Test Dismiss Alert...")
        time.sleep(1)

        # press Confirm button then popup to be showed
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(1)

        # Dismiss
        alert2 = driver.switch_to.alert
        alert2.accept()
        time.sleep(2)


        # input some text to search box
        driver.find_element_by_id("name").send_keys("Test Read a text from the Alert...")
        time.sleep(1)

        # press Confirm button then popup to be showed
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(1)

        # Reading a the text of a prompt for verification:
        alert4 = driver.switch_to.alert.text
        print(str(alert4))
        time.sleep(2)

        alert5 = driver.switch_to.alert
        alert5.dismiss()
        time.sleep(2)

        driver.quit()

ff = SwitchToAlert()
ff.test()