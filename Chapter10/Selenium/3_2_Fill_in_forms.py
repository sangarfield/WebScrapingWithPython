from selenium import webdriver
from selenium.webdriver.support.ui import Select
url = "http://www.google.com"
xpath = "//fieldset/input[@name='q']"

driver = webdriver.Chrome()
driver.get(url)
'''
ele = driver.find_element_by_xpath("//input[@id ='id-search-field']")

#ele = driver.find_element_by_id("id-search-field")
print(ele)
'''
ele = driver.find_element_by_xpath("//div[@id='sfdiv']//input[@class='gsfi']")
ele.send_keys('cute dog')
select = Select(driver.find_element_by_xpath("//center/input[@type='submit']"))
driver.find_element_by_xpath("//center/input[@type='submit']").click()
