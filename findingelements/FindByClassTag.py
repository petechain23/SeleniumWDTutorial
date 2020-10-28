from selenium import webdriver


class FindByClassTag():
    def test(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")

        elementByClass = driver.find_element_by_class_name("inputs")
        elementByClass.send_keys('Input something here!')
        if elementByClass is not None:
            print("we found an element by Class")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text
        if elementByTagName is not None:
            print("we found an element by Tag Name " + text)


ff = FindByClassTag()
ff.test()
