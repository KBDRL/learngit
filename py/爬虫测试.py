import requests
from bs4 import BeautifulSoup as bs4


def tianya(url):
    '''这是一个爬虫测试'''
    masg = '配方'
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = bs4(res.text, 'html.parser')
    cl = []
    for news in html.select('.bbs-content'):
        if masg in news.text:
            m = news.text
            t = m.split(' ')
            for i in t:
                if masg in i:
                    cl.append(i)

    print(cl)

# url = 'http://bbs.tianya.cn/post-no11-1091565-3.shtml'
# tianya(url)
for n in range(124):
    url = 'http://bbs.tianya.cn/post-no11-1091565-' + str(n) + '.shtml'
    tianya(url)
