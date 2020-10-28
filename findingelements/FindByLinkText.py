from selenium import webdriver


class FindByLinkText():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        title = driver.title
        print(title)
        elementByLinkText = driver.find_element_by_link_text("Login")
        if elementByLinkText is not None:
            print("we found an element by element By Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Prac")
        if elementByPartialLinkText is not None:
            print("we found an element by element By Partial Link Text")


ff = FindByLinkText()
ff.test()
