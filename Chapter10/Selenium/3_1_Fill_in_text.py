'''
    在google上搜索cute dog
    清除文本框
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.google.com")

ele = driver.find_element_by_id("lst-ib")
ele.send_keys("cute")

ele.send_keys(" dog", Keys.RETURN)

sleep(5)

ele.clear()

sleep(5)

driver.close()

