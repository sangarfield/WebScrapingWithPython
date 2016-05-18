'''
    向表单上传文件
'''
import requests

url = 'http://pythonscraping.com/pages/processing2.php'
params = {'uploadFile' : open(r"C:/py.png", 'rb')}  #open打开
r = requests.post(url, files = params) #files参数
print(r.text)