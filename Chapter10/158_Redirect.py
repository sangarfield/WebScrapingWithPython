from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitLoad(driver):
    ele = driver.find_element_by_tag_name("html")
    print(driver)
    count = 0
    while True:
        count += 1
        if count > 10:
            print("timeout")
            return
        time.sleep(0.5)
        try:
            elem = driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\phantomjs.exe")
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo2.html")
waitLoad(driver)
print(driver.page_source)