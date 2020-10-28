from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonAndCheckboxes():
    def test(self):

        options = webdriver.FirefoxOptions()
        options.set_preference("permissions.default.desktop-notification", 1)
        # options.set_preference("dom.push.enabled", False)
        driver = webdriver.Firefox(options=options)

        baseUrl = "https://www.vietjetair.com/Sites/Web/vi-VN/Home"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # RbOneWay
        radioBtnOneWay = driver.find_element(By.ID, "#ctl00_UcRightV31_RbOneWay")
        radioBtnOneWay.click()
        print("One Way button is selected" + radioBtnOneWay.is_selected())

        # RbRoundTrip
        time.sleep(2)
        radioBtnRoundTrip = driver.find_element(By.CSS_SELECTOR, "#ctl00_UcRightV31_RbRoundTrip")
        radioBtnRoundTrip.click()
        print("Round Trip button is selected" + radioBtnRoundTrip.is_selected())

        # ChkInfare
        time.sleep(2)
        radioBtnCheckGiaRe = driver.find_element(By.ID, "#ctl00_UcRightV31_ChkInfare")
        radioBtnCheckGiaRe.click()
        print("Check box gia re is selected" + radioBtnCheckGiaRe.is_selected())

        # BoCheckGiaRe
        time.sleep(2)
        radioBtnCheckGiaRe.click()
        print("Check box gia re is unselected" + radioBtnRoundTrip.is_selected())

        driver.quit()
ff = RadioButtonAndCheckboxes()
ff.test()