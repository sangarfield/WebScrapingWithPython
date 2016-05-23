from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("http://www.google.com")

try:
    element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(By.ID, r"sfdiv")
    print(element)
finally:
    driver.quit()