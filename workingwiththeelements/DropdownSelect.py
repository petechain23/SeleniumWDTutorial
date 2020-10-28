from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        dropdownList = driver.find_element_by_id("carselect")
        select = Select(dropdownList)

        bmw = select.select_by_value('bmw')
        print('bmw is selected')
        time.sleep(3)

        benz = select.select_by_visible_text('benz')
        print('benz is selected')
        time.sleep(3)

        honda = select.select_by_index('2')
        print('honda is selected')
        time.sleep(3)


ff = DropdownSelect()
ff.test()