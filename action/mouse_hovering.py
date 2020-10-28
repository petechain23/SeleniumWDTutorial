from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MouseHovering():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.title

        driver.execute_script("window.scrollBy(0, 1000);")
        element = driver.find_element_by_id("mousehover")
        time.sleep(2)
        itemToClickLocation = './/div[@class="mouse-hover-content"]//a[text()="Top"]'

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse hover element")
            time.sleep(2)

            topLink = driver.find_element(By.XPATH, itemToClickLocation)
            actions.move_to_element(topLink).click().perform()
            print("Clicked")
            time.sleep(2)
        except:
            print("Mouse Hover failed on element")

        driver.quit()

ff = MouseHovering()
ff.test()