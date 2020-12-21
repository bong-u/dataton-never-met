# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class movie_data:
    def __init__(self, title, date, offline, online):
        self.title = title
        self.date = date
        self.offline = offline
        self.online = online
        self.ratio = round(int(offline.replace(",",""))/int(online.replace(",","")),2)

url = 'http://www.kobis.or.kr/kobis/business/stat/online/onlineYearlyBoxRank.do?CSRFToken=fMV3gtByZkRCnU8eIcRanC_c4y5H83RVU_nN3Jqzw6I&curPage=1&loadEnd=0&searchType=search&sSearchYearFrom=2020&sMultiMovieYn='
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
text = soup.text.strip()
title_list = soup.select("#table > tbody > tr > td > a > span")
date_list = soup.select("#table > tbody > tr > td:nth-child(4)")
offline_list = soup.select("#table > tbody > tr > td:nth-child(10)")
online_list = soup.select("#table > tbody > tr > td:nth-child(11)")
movie_data_ob = []

before = [] #2020년 전 영화
after = []  #2020년 이후 영화

for i in range(len(title_list)):
    m1 = movie_data(title_list[i].text, date_list[i].text, offline_list[i].text, online_list[i].text)
    movie_data_ob.append(m1)
for i in movie_data_ob:
    year = i.date[0:4]
    if int(year) < 2020:
        before.append(i)
    else:
        after.append(i)


print("************************************2020년 전 영화************************************")
print()
before_sum = 0
after_sum = 0
for i in before:
    print(i.title)
    print(i.date)
    print(i.ratio)
    before_sum += i.ratio
print()
print("************************************2020년 이후 영화************************************")
for i in after:
    print(i.title)
    print(i.date)
    print(i.ratio)
    after_sum += i.ratio
print(f'2020년 전 영화      오프라인 이용 수 / 온라인 이용 수 평균 : {before_sum/len(before)}')
print(f'2020년 이후 영화      오프라인 이용 수 / 온라인 이용 수 평균 : {after_sum/len(after)}')