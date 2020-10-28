from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class ScrollingElement():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        title = driver.execute_script('return document.title;')
        print(title)
        #Scroll Down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
        #scroll Up
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)

        #scroll element by Id mousehover in to view
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -150);")

        #Native Way To scroll element into view
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))

        # driver.quit()

ff =ScrollingElement()
ff.test()