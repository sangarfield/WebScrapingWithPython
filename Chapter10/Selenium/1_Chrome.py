from selenium import webdriver

url = r"www.baidu.com"
broswer = webdriver.Chrome()
broswer.get(url)
print(broswer.title)