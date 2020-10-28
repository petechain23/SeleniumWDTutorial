from selenium import webdriver
import time

class AutoComplete():
    def test1(self):
        driver = webdriver.Firefox()
        baseUrl = "http://www.southwest.com"
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        textinput = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
        textinput.send_keys("New York")
        time.sleep(3)
        autocomplete = driver.find_element_by_class_name("flyout-portal")
        driver.find_element_by_xpath("/html/body")
        autocomplete.click()

ff = AutoComplete()
ff.test1()