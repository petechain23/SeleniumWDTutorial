from selenium import webdriver
import advanced.screenshots as screenshot
class WindowSize():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(baseUrl)
        driver.title
        '''e.g 1
        java script'''
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Window Height: " +str(height))
        print("Window Width: "  +str(width))

        '''e.g 2 
        web driver'''
        window_size = driver.get_window_size()
        print("Window size: " + str(window_size))

        sc = screenshot.ScreenShots()
        sc.takeScreenshot(driver)

        driver.quit()
ff = WindowSize()
ff.test()