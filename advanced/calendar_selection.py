from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class CalendarSelection():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://www.expedia.com"
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        driver.title
        driver.maximize_window()

        flight_tab = driver.find_element(By.XPATH, "//ul[@id='uitk-tabs-button-container']/li[2]/a[@role='tab']/span[@class='uitk-tab-text']")
        getinfo = flight_tab.click()

        driver.find_element(By.ID, "d1-btn").click()

        time.sleep(3)
        driver.quit()

ff = CalendarSelection()
ff.test()