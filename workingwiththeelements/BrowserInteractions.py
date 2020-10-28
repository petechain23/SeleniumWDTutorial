from selenium import webdriver

class BrowserInteractions():

    def test(self):
        try:
            baseUrl = "https://letskodeit.teachable.com/pages/practice"
            driver = webdriver.Firefox()

            # Window Maximize
            driver.maximize_window()
            # Open the Url
            openUrl = driver.get(baseUrl)
            # Get Title
            getTitle = driver.title
            print(getTitle)
            # Get Current Url
            get_Current_Url = driver.current_url
            print(get_Current_Url)
            # Browser Refresh
            refresh = driver.refresh()
            # Open another Url
            openUrl = driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
            # Browser Back
            back = driver.back()
            getTitle = driver.title
            print(getTitle)
            # Browser Forward
            forward = driver.forward()
            getTitle = driver.title
            print(getTitle)
            # Get Page Source
            source_page = driver.page_source
            print(str(source_page))
        except:
            print('Failed')
        finally:
            # Browser Close / Quit
            # driver.close()
            driver.quit()
            driver.find_element().click()

ff = BrowserInteractions()
ff.test()