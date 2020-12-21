# -*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://yshs.djsch.kr/boardCnts/list.do?boardID=83972&m=090431&s=yuseonghs#contents'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'lxml')
topic = soup.select('td[class = link]')   # topic = [Atom설치 보충 설명, 크롤러 프레임 코드 업데이트, 크롤러 코드입니다.(셀프 코드리뷰), -----]

real_topic = topic[7:14]

r = 1
for i in real_topic:
    name = i.text.strip()
    print(str(r)+ '    ' + name)
    r = r + 1
