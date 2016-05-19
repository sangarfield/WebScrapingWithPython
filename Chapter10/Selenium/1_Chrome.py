from selenium import webdriver

url = r"www.baidu.com"
broswer = webdriver.Chrome()
broswer.get('http://www.zhihu.com')
print(broswer.title)