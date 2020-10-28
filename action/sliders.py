from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import advanced.screenshots as screenshot

class Sliders():
    def test(self):
        baseUrl = "https://jqueryui.com/slider"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.title

        # select frame contain slider element
        driver.switch_to.frame(0)
        slider = driver.find_element_by_id("slider")
        try:
            actions = ActionChains(driver)
            # slider bar
            actions.drag_and_drop_by_offset(slider, 100, 0).perform()
            print("Slider element successful")
            sc = screenshot.ScreenShots()
            sc.takeScreenshot(driver)
            time.sleep(2)
        except:
            print("Failed on element")

        driver.quit()


ff = Sliders()
ff.test()
