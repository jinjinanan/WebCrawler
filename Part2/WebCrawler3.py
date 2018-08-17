# 收集整个网站
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageURL):
    '''
    采集整个网站
    :param pageURL:
    :return:
    '''
    global pages
    html = urlopen('http://en.wikipedia.org' + pageURL)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except:
        print('页面缺少')
    for link in bsObj.findAll('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('------------\n'+newPage)
                pages.add(newPage)
                getLinks1(newPage)

getLinks('')
