from selenium import webdriver

url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

import time
driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\phantomjs.exe")
driver.get(url)
time.sleep(1)
print(driver.find_element_by_id('content').text)
driver.close()