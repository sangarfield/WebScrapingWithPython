from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")
ele = driver.find_element_by_xpath("//select[@name='name']")
options = ele.find_element_by_tag_name("option")
for opt in options:
    print(opt.get_atrribute("value"))
    opt.click()

driver.close()
