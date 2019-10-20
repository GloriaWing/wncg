# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import csv
import codecs


pages=6 #在此修改需要爬取的页数，每页20条新闻

url = 'https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&\
versionNumber=1.2.4&page={}&encode=utf-8&callback=feedCardJsonpCallback&_=1568108608385'
 
commentUrl = 'https://comment.sina.com.cn/page/info?version=1&format=json\
&channel=gn&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8\
&page=1&page_size=3&t_size=3&h_size=3&thread=1&uid=3537461634'


def ReadFile(filePath,encoding="utf-8"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()
 
def WriteFile(filePath,u,encoding="gbk"):
    with codecs.open(filePath,"w",encoding) as f:
        f.write(u)
 
def UTF8_2_GBK(src,dst):  #将爬取后保存的UTF-8编码的网页内容转化成GBK编码的文件，让excle可以直接打开
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gb18030")


#获取新闻页内关键信息
def Get_news(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf=8'
    soup = BeautifulSoup(res.text,"lxml")
    result['title'] = soup.select('.main-title')[0].text
    timesource = soup.select('.date-source')[0].select('.date')[0].text  
    result['time'] = timesource
    result['origin'] = soup.select('.date-source a')[0].text
    result['article'] = '  '.join([p.text.strip() for p in soup.select('#article p')[:-1]])
    result['author'] = soup.select('.show_author')[0].text.lstrip('责任编辑：')  #删去责任编辑关键字，直接显示编辑姓名
    result['comments'] = Get_Comments(newsurl)
    return result
#获取评论数量
def Get_Comments(newsulr):
    m = re.search('doc-i(.+).shtml',newsulr)
    news_Id = m.group(1)
    comment_url = commentUrl.format(news_Id)
    comments = requests.get(comment_url)
    jd = json.loads(comments.text)
    return jd['result']['count']['total']
 
#获取每个分页的所有新闻的URL，然后取得详细信息
def page_links(url):
    newsdetails = []
    res = requests.get(url)
    res = res.text.split("try{feedCardJsonpCallback(")[1].split(");}catch(e){};")[0]
    jd = json.loads(res)
    for item in jd['result']['data']:
        newsdetails.append(Get_news(item['url']))
    return newsdetails


if __name__ == '__main__':  
    news_total = []
    for i in range(1,pages+1):    #根据页数获得信息
        print('正在爬取第 {} 页新闻...'.format(i))
        news_url = url.format(i)
        news_dict = page_links(news_url)
        news_total.extend(news_dict)
    print('爬取总共获得新闻',len(news_total),'条')
   
    headers = ['title','time','origin','author','comments','article']    
    with open('temp.csv','w',encoding="utf-8",newline='')as f:
        f_csv = csv.DictWriter(f,headers)
        f_csv.writeheader()   #将表头写入csv
        f_csv.writerows(news_total)  #将对应的信息根据dict名称写入
        
    UTF8_2_GBK('temp.csv','test_finall.csv') #把编码格式转化为windows下的GBK以便excle直接查看



    


