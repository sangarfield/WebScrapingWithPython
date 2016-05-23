from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'http://www.python.org'

broswer = webdriver.Chrome()
broswer.get(url)
assert "Python" in broswer.title
ele = broswer.find_element_by_id("id-search-field")
ele.send_keys("sorted")
ele.send_keys(Keys.RETURN)
print(broswer.page_source)

print("where")