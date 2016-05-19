from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'
driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\phantomjs.exe")
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(by.id, "loadedButton"))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()
