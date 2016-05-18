'''
    从网页读取一段，分析语义，两个单词为一个组
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

def ngrams(input, n):
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