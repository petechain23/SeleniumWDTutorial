from selenium import webdriver
import time

class WorkingWithElementsList():
    def testListElements(self):
        driver = webdriver.Firefox()
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        listElements = driver.find_elements_by_xpath('//input[contains(@name,"cars") and contains(@type,"radio")]')
        size = len(listElements)
        print('Size of list: ' + str(size))
        for element in listElements:
            select = element.is_selected()
            if not select:
                element.click()
                time.sleep(2)

        driver.quit()
ff = WorkingWithElementsList()
ff.testListElements()