from selenium import webdriver
from datetime import datetime
import time
class ScreenShots():
    def test1(self):
        # chrome://version/
        # opt = webdriver.ChromeOptions()
        # opt.add_argument("/Users/dattran/Library/Application Support/Google/Chrome/Default")
        # baseUrl = "https://letskodeit.teachable.com/"
        # driver = webdriver.Chrome(options=opt)

        baseUrl = "https://courses.letskodeit.com/login"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.title

        # driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("email").send_keys("username@123.com")
        driver.find_element_by_id("password").send_keys("pw123456")
        driver.find_element_by_xpath("//form/div[4]/div[1]/input").click()
        time.sleep(10)
        #
        self.takeScreenshot(driver)
        driver.quit()

    def takeScreenshot(self, driver):
        now = datetime.now()
        # dd/mm/YY H:M:S
        fileName = now.strftime("%d%m%Y%H%M%S")
        destinationFile = "../Screenshots/%s.png" %fileName
        try:
            driver.save_screenshot(destinationFile)
            print("A new Screenshot name:: "+fileName)
        except NotADirectoryError:
            print("Cannot save screenshot with direction")

ff = ScreenShots()
# ff.test1()