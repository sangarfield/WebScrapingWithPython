'''
    结合cookie进行访问
'''
import requests

url = 'http://pythonscraping.com/pages/cookies/welcome.php'
params = {'username' : 'Kevin', 'password' : 'password'}

r = requests.post(url, data = params)
print(r.cookies.get_dict()) #获取了登陆后得到的cookie
print(r.cookies)
url = 'http://pythonscraping.com/pages/cookies/profile.php'
r = requests.get(url, cookies = r.cookies) #添加cookie
print(r.text)


