from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class DragAndDrop():
    def test(self):
        baseUrl = "https://jqueryui.com/droppable"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.title

        # select frame contain element to drop and drag
        driver.switch_to.frame(0)
        draggable = driver.find_element_by_id("draggable")
        droppable = driver.find_element_by_id("droppable")

        try:
            actions = ActionChains(driver)
            # Drag and drop
            # actions.drag_and_drop(draggable, droppable).perform()
            # print("Drag and drop successful")

            # click and hold
            actions.click_and_hold(draggable).move_to_element(droppable).release().perform()
            print("Click and hold successful")
            time.sleep(2)

        except:
            print("Drag and drop failed on element")

        driver.quit()

ff = DragAndDrop()
ff.test()