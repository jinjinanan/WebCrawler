from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

def crawl_static():
    html = urlopen('http://jr.jd.com')
    #   把html内容导入BeautifulSoup对象
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    print(html.read())
    text_list = bs_obj.find_all('a', 'nav-item-primary')
    for text in text_list:
        print(text.get_text())
    html.close()

def crawl_active():
    url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
    # 用PhantomJS
    driver = webdriver.PhantomJS()
    csv_file = open('playList.csv','w',newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['标题','播放数','链接'])

    # 解析每一页，知道'下一页'为空
    while url != 'javascript:void(0)':
        # 用WebDriver加载页面
        driver.get(url)
        # 切换到内容iframe
        driver.switch_to.frame('contentFrame')
        # 定位歌单标签
        data = driver.find_element_by_id('m-pl-container').\
            find_elements_by_tag_name('li')
        # 解析一页中的所有歌单
        for i in range(len(data)):
            # 获取播放数
            nb = data[i].find_element_by_class_name('nb').text
            if '万' in nb and int(nb.split('万')[0]) > 500:
                # 获取播放数大于500万的歌单封面
                msk = data[i].find_element_by_css_selector('a.msk')
                # 把封面伤的标题和链接同播放数一起写到文件中
                writer.writerow(
                    [msk.get_attribute('title'),
                     nb,
                     msk.get_attribute('href')]
                )
        # 定位'下一页'中的url
        url = driver.find_element_by_css_selector('a.zbtn.znxt'). \
            get_attribute('href')
    csv_file.close()

crawl_active()




