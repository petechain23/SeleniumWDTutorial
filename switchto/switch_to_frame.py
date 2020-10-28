from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.title
        # scroll page to Frame content
        driver.execute_script("window.scrollBy(0, 1500);")

        # swtch to Frame using ID
        driver.switch_to.frame("courses-iframe")
        # swtch to Frame using name
        # driver.switch_to.frame("iframe-name")
        # swtch to Frame using Number
        # driver.switch_to.frame(0)
        time.sleep(2)

        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(2)

        # switch to main Frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1500);")
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("Test complete")
        time.sleep(2)

        driver.quit()

ff = SwitchToFrame()
ff.test()