from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo():
    def test(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("we found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("we found an element by Xpath")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("we found an element by element By Link Text")


ff = ByDemo()
ff.test()
