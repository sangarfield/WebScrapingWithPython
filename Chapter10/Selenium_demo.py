from selenium import webdriver

broswer = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")
broswer.get("http://www.google.com")
print(broswer)