'''
    填写一个提交表单
    http://pythonscraping.com/pages/files/form.html
'''
import requests

url = 'http://pythonscraping.com/files/processing.php'
params = {'firstname' : 'Kevin', 'lastname' : 'Liu'}
r = requests.post(url, params)
print(r.text)