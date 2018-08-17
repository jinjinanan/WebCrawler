from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import random
import datetime

random.seed(datetime.datetime.now())
# csv_file = open('link.csv','w',newline='')
# writer = csv.writer(csv_file)
# writer.writerow(['链接'])

def getlinks(articleURL):
    html = urlopen('http://en.wikipedia.org'+articleURL)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div',{'id':'bodyContent'}).\
        findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getlinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    # writer.writerow(newArticle)
    print(newArticle)
    links= getlinks(newArticle)
# csv_file.close()