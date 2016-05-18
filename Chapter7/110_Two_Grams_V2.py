'''
    从网页读取一段，分析语义，两个单词为一个组
    正则表达式去除换行、多空格
    utf-8去除转义字符
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def ngrams(input, n):
    input = re.sub('\n+', ' ', input)
    input = re.sub(' +', ' ', input)
    '''
    re.sub(pattern, repl, string, count=0, flags=0)
            模式    替换成  被替换
    '''

    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    #bytes.decode(encoding="utf-8", errors="strict")
    #                解码            错误处理

    input = input.split(' ')

    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i : i + n])

    return output

url = r'http://en.wikipedia.org/wiki/Python'
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
output = ngrams(content, 2)
print(output)