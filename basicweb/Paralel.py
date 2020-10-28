from selenium import webdriver
from basicweb import chrome_driver_mac
from basicweb import firefox_driver_mac
from basicweb import safari_driver_mac

driver = chrome_driver_mac.ChromeDriverMac()
driver.testMethod()