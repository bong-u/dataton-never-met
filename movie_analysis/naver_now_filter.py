#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import sys
import io
#
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%8B%A4%EA%B2%80'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
k = soup.select("#sub_pack > section.sc_new.sp_nkeyword.type_news > div > div.hot_keyword_srch._aside_news_tab > div:nth-child(2) > ol > li > a > span")
now = []
for i in k:
    now.append(i.text)
for i in now:
    if "식당"in i:
        print(i)
    elif "코로나"in i:
        print(i)
    elif "배달"in i:
        print(i)
    elif "집콕"in i:
        print(i)
    elif "홈시어터"in i:
        print(i)
    elif "맛집"in i:
        print(i)
    elif "거리두기"in i:
        print(i)
    elif "확진"in i:
        print(i)
