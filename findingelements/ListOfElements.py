from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements():
    def test(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassName)
        if elementListByClassName is not None:
            print("ClassName -> Size of the list is: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)
        if elementListByClassName is not None:
            print("TagName -> Size of the list is: " + str(length2))


ff = ListOfElements()
ff.test()
