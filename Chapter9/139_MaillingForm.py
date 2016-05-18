'''
    填写一个提交表单
'''
import requests

url = 'http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi'

params = {'email_addr': 'sangarfield@qq.com'}
r = requests.post(url, data = params)
print(r.text)