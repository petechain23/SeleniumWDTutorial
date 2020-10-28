from selenium import webdriver


class FindByXpathCss():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByXpath = driver.find_element_by_xpath('//input[@id="name"]')
        if elementByXpath is not None:
            print("we found an element by Xpath")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")
        if elementByCss is not None:
            print("we found an element by Css")

        driver.quit()

ff = FindByXpathCss()
ff.test()
