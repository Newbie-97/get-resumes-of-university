# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:15:54 2018

@author: Ezreal
"""
#此代码主要针对在高校爬取到的简历进行男女各数量的统计

import requests
import time 
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

s = requests.Session()
s.cookies = CookieJar()

#登录URL
login_url = 'http://njue.91job.gov.cn/vip/user/login'
#爬取时的URL
start_url = 'http://njue.91job.gov.cn/vip/talents/search/domain/njue/page/'

#发起POST请求的函数
def urlPOST(loginurl):
    try:
        #构建头部
        header={
                'User-Agent':'Baiduspider+',
                }
        
        data = {
                'username':'xxxxxx有限责任公司',
                'password':'********',
                }
        
        s.post(url = loginurl, headers=header , data = data)
    except:
        print('urlPOST Error!')

#编写程序:根据URL获取HTML
def getHTML(url,code='utf-8'):
    try:
        urlPOST(login_url)
        r = s.get(url,timeout=20)
        r.raise_for_status()
        r.coding = code
        return r.text
    except:
        print('getHTML Error!')
        
def startRUN():
    try:
        man , woman = 0 , 0
        #开始/结束爬取的页数
        start_page = int(input('Please input beginning page :'))
        end_page = int(input('Please input ending page :'))
        #开始爬取
        for page in range(start_page,end_page+1):
            #URL由start_url和页数组合而成
            url = start_url + str(page)
            #获取html
            html = getHTML(url)
            #构建BeautifulSoup
            soup = BeautifulSoup(html,'lxml')
            html_sex = soup.find_all( class_ ='span5')
            
            #获取到的html_sex为列表
            #如果是男生则man加1，反之是女生的话，woman加1
            for sex in html_sex:
                if '男' in sex :
                    man = man + 1
                elif '女' in sex :
                    woman = woman + 1
                    
            #打印进度
            print('\r ---第%s页采取成功---'%page, end=' ')
        
        print('\n')
        print('男生数量：%s'%man)    
        print('女生数量：%s'%woman)
            
    except:
        print('startRUN Error!')

if __name__ == '__main__':
    startRUN()
        