from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from advanced import screenshots

class SwitchToWindow():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.title

        # find parent handle -> main window
        parentHandle = driver.current_window_handle
        print("Main window: " + parentHandle)
        # Click open new window
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(3)
        # find all handles, there should two window handles after clicking open window button
        handles = driver.window_handles
        time.sleep(3)
        # switch to window and search course
        for handle in handles:
            print("Windows ID: " + str(handle))
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Child window: " + handle)
                # find search textbox and search a course
                driver.find_element(By.ID, "search-courses").send_keys("Python 3")
                screenshots.ScreenShots.takeScreenshot(driver)
                time.sleep(2)
                driver.close()
                break
        driver.switch_to.window(parentHandle)
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test success")
        time.sleep(2)
        print("Test complete")
        driver.quit()


ff = SwitchToWindow()
ff.test()