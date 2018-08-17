from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import random
import datetime

pages = set()
def getLinks1(pageURL):
    '''
    采集整个网站
    :param pageURL:
    :return:
    '''
    global pages
    html = urlopen('http://en.wikipedia.org' + pageURL)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks1(newPage)

getLinks1('')