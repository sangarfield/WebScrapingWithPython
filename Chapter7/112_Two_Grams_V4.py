'''
    从网页读取一段，分析语义，两个单词为一个组
    正则表达式去除换行、多空格
    utf-8去除转义字符

    去除单独的字母，除了i和a
    维基百科的引用标识（括号间的数字）应该被去除
    标点符号应该被去除

    V4
    使用OrderedDict来排序
    排除大小写的区别
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import string
from collections import OrderedDict

def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]+\]', '', input)
    input = re.sub(' +', ' ', input)

    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    #bytes.decode(encoding="utf-8", errors="strict")
    #                解码            错误处理
    cleanInput = []
    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation) #去除标点符号
        if len(item) > 1 or (item.lower() == 'i' or item.lower() == 'a'): #只用长度大于1或者i或者a
            cleanInput.append(item.upper()) #排除大小写
    return cleanInput


def ngrams(input, n):

    input = cleanInput(input)

    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i : i + n])

    return output

url = r'http://en.wikipedia.org/wiki/Python'
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
output = ngrams(content, 2)

output = OrderedDict(sorted(output, key = lambda t : t[1], reverse = True)) #有序字典，无重复的元素

print(output)