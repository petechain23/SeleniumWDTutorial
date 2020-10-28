from selenium import webdriver

class FindByIdName():
    def test(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")

        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print("we found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")
        if elementByName is not None:
            print("we found an element by Name")

        driver.quit()

ff = FindByIdName()
ff.test()
