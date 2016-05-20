from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert 'Python' in driver.title

elem = driver.find_element_by_id("id-search-field")
elem.send_keys("add")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()