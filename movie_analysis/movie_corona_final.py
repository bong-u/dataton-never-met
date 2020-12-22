import pandas as pd
import matplotlib.pyplot as plt
# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class movie_data:
    def __init__(self, title, date, offline, online):
        self.title = title
        self.date = date
        self.offline = offline
        self.online = online
        self.ratio = round(int(offline.replace(",", "")) / int(online.replace(",", "")), 2)


movie_data_ob = []  # movie_data를 저장할 객체 리스트
before = []  # 2020년 전 영화
after = []  # 2020년 이후 영화
#월별로 나눠서 저장할 객체 리스트
y19_m8 = []
y19_m9 = []
y19_m10 = []
y19_m11 = []
y19_m12 = []
y20_m1 = []
y20_m2 = []
y20_m3 = []
y20_m4 = []
y20_m5 = []
y20_m6 = []
y20_m7 = []
y20_m8 = []
etc = []
# 2020년 기준 조회 1~25위 영화 크롤링
url = 'http://www.kobis.or.kr/kobis/business/stat/online/onlineYearlyBoxRank.do?CSRFToken=fMV3gtByZkRCnU8eIcRanC_c4y5H83RVU_nN3Jqzw6I&curPage=1&loadEnd=0&searchType=search&sSearchYearFrom=2020&sMultiMovieYn='
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
text = soup.text.strip()
title_list = soup.select("#table > tbody > tr > td > a > span")
date_list = soup.select("#table > tbody > tr > td:nth-child(4)")
offline_list = soup.select("#table > tbody > tr > td:nth-child(10)")
online_list = soup.select("#table > tbody > tr > td:nth-child(11)")
#2020년 기준 조회 영화 추가
for i in range(len(title_list)):
    marker = 0
    for j in movie_data_ob:
        if j.title == title_list[i]:
            marker = 1
    if marker == 0 and online_list[i] != 0:
        m1 = movie_data(title_list[i].text, date_list[i].text, offline_list[i].text, online_list[i].text)
        movie_data_ob.append(m1)

# 2019년 기준 조회 1~25위 영화 크롤링
url = 'http://www.kobis.or.kr/kobis/business/stat/online/onlineYearlyBoxRank.do?CSRFToken=fMV3gtByZkRCnU8eIcRanC_c4y5H83RVU_nN3Jqzw6I&curPage=1&loadEnd=0&searchType=search&sSearchYearFrom=2019&sMultiMovieYn='
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
text = soup.text.strip()
title_list = soup.select("#table > tbody > tr > td > a > span")
date_list = soup.select("#table > tbody > tr > td:nth-child(4)")
offline_list = soup.select("#table > tbody > tr > td:nth-child(10)")
online_list = soup.select("#table > tbody > tr > td:nth-child(11)")
#2019년 기준 조회 영화 추가
for i in range(len(title_list)):
    marker = 0
    for j in movie_data_ob:
        if j.title == title_list[i]:
            marker = 1
    if marker == 0 and online_list[i] != 0:
        m1 = movie_data(title_list[i].text, date_list[i].text, offline_list[i].text, online_list[i].text)
        movie_data_ob.append(m1)

#2020년 기준 전후 나눔
for i in range(len(title_list)):
    m1 = movie_data(title_list[i].text, date_list[i].text, offline_list[i].text, online_list[i].text)
    movie_data_ob.append(m1)
for i in movie_data_ob:
    year = int(i.date[0:4])
    if year < 2020:
        before.append(i)
    else:
        after.append(i)
#2020년 기준 전후 비율 평균 구하기
before_sum = 0
after_sum = 0
for i in before:
    before_sum += i.ratio

for i in after:
    after_sum += i.ratio
avg_ratio_after = round(after_sum / len(after), 2)
avg_ratio_before = round(before_sum / len(before), 2)
#개봉일 기준으로 월별로 나누기
for i in movie_data_ob:
    year = int(i.date[0:4])
    month = i.date[5:7]
    if year == 2019:
        if month == "08":
            y19_m8.append(i)
        elif month == "09":
            y19_m9.append(i)
        elif month == "10":
            y19_m10.append(i)
        elif month == "11":
            y19_m11.append(i)
        elif month == "12":
            y19_m12.append(i)
        else:
            etc.append(i)
    elif year == 2020:
        if month == "01":
            y20_m1.append(i)
        elif month == "02":
            y20_m2.append(i)
        elif month == "03":
            y20_m3.append(i)
        elif month == "04":
            y20_m4.append(i)
        elif month == "05":
            y20_m5.append(i)
        elif month == "06":
            y20_m6.append(i)
        elif month == "07":
            y20_m7.append(i)
        elif month == "08":
            y20_m8.append(i)
        else:
            etc.append(i)
    else:
        etc.append(i)
#월별 오프라인/온라인 비율 평균 구하기
sum = 0
for i in y19_m8:
    sum += i.ratio
if len(y19_m8) != 0:
    avg_ratio_y19_m8 = round(sum / len(y19_m8), 2)
else:
    avg_ratio_y19_m8 = 0
sum = 0
for i in y19_m9:
    sum += i.ratio
if len(y19_m9) != 0:
    avg_ratio_y19_m9 = round(sum / len(y19_m9), 2)
else:
    avg_ratio_y19_m9 = 0
sum = 0
for i in y19_m10:
    sum += i.ratio
if len(y19_m10) != 0:
    avg_ratio_y19_m10 = round(sum / len(y19_m10), 2)
else:
    avg_ratio_y19_m10 = 0
sum = 0
for i in y19_m11:
    sum += i.ratio
if len(y19_m11) != 0:
    avg_ratio_y19_m11 = round(sum / len(y19_m11), 2)
else:
    avg_ratio_y19_m11 = 0
sum = 0
for i in y19_m12:
    sum += i.ratio
if len(y19_m12) != 0:
    avg_ratio_y19_m12 = round(sum / len(y19_m12), 2)
else:
    avg_ratio_y19_m12 = 0
sum = 0
for i in y20_m1:
    sum += i.ratio
if len(y20_m1) != 0:
    avg_ratio_y20_m1 = round(sum / len(y20_m1), 2)
else:
    avg_ratio_y20_m1 = 0
sum = 0
for i in y20_m2:
    sum += i.ratio
if len(y20_m2) != 0:
    avg_ratio_y20_m2 = round(sum / len(y20_m2), 2)
else:
    avg_ratio_y20_m2 = 0
sum = 0
for i in y20_m3:
    sum += i.ratio
if len(y20_m3) != 0:
    avg_ratio_y20_m3 = round(sum / len(y20_m3), 2)
else:
    avg_ratio_y20_m3 = 0
sum = 0
for i in y20_m4:
    sum += i.ratio
if len(y20_m4) != 0:
    avg_ratio_y20_m4 = round(sum / len(y20_m4), 2)
else:
    avg_ratio_y20_m4 = 0
sum = 0
for i in y20_m5:
    sum += i.ratio
if len(y20_m5) != 0:
    avg_ratio_y20_m5 = round(sum / len(y20_m5), 2)
else:
    avg_ratio_y20_m5 = 0
sum = 0
for i in y20_m6:
    sum += i.ratio
if len(y20_m6) != 0:
    avg_ratio_y20_m6 = round(sum / len(y20_m6), 2)
else:
    avg_ratio_y20_m6 = 0
sum = 0
for i in y20_m7:
    sum += i.ratio
if len(y20_m7) != 0:
    avg_ratio_y20_m7 = round(sum / len(y20_m7), 2)
else:
    avg_ratio_y20_m7 = 0
sum = 0
for i in y20_m8:
    sum += i.ratio
if len(y20_m8) != 0:
    avg_ratio_y20_m8 = round(sum / len(y20_m8), 2)
else:
    avg_ratio_y20_m8 = 0
sum = 0
for i in etc:
    sum += i.ratio
if len(etc) != 0:
    avg_ratio_etc = round(sum / len(etc), 2)
else:
    avg_ratio_etc = 0
'''
#결과 출력
print(f'2019.8월 전 기타 평균 : {avg_ratio_y19_m8}')
print(f'2019.9 평균 : {avg_ratio_y19_m9}')
print(f'2019.10 평균 : {avg_ratio_y19_m10}')
print(f'2019.11 평균 : {avg_ratio_y19_m11}')
print(f'2019.12 평균 : {avg_ratio_y19_m12}')
print(f'2020.1 평균 : {avg_ratio_y20_m1}')
print(f'2020.2 평균 : {avg_ratio_y20_m2}')
print(f'2020.3 평균 : {avg_ratio_y20_m3}')
print(f'2020.4 평균 : {avg_ratio_y20_m4}')
print(f'2020.5 평균 : {avg_ratio_y20_m5}')
print(f'2020.6 평균 : {avg_ratio_y20_m6}')
print(f'2020.7 평균 : {avg_ratio_y20_m7}')
print(f'2020.8 평균 : {avg_ratio_y20_m8}')
'''
result_ratio = []
result_ratio.append(avg_ratio_y19_m8)
result_ratio.append(avg_ratio_y19_m9)
result_ratio.append(avg_ratio_y19_m10)
result_ratio.append(avg_ratio_y19_m11)
result_ratio.append(avg_ratio_y19_m12)
result_ratio.append(avg_ratio_y20_m1)
result_ratio.append(avg_ratio_y20_m2)
result_ratio.append(avg_ratio_y20_m3)
result_ratio.append(avg_ratio_y20_m4)
result_ratio.append(avg_ratio_y20_m5)
result_ratio.append(avg_ratio_y20_m6)
result_ratio.append(avg_ratio_y20_m7)
result_ratio.append(avg_ratio_y20_m8)

df1 = pd.read_excel('./total_corona_count.xlsx',  usecols="A:F")
case = df1['일일확진자수'].tolist()

c_03 = 0
c_04 = 0
c_05 = 0
c_06 = 0
c_07 = 0
c_08 = 0
c_09 = 0
c_10 = 0
c_11 = 0
c_12 = 0

for i in range(len(case)):
    if(i<=26):
        c_03 += case[i]
    elif(i<=57):
        c_04 += case[i]
    elif(i<=87):
        c_05 += case[i]
    elif(i<=117):
        c_06 += case[i]
    elif(i<=148):
        c_07 += case[i]
    elif(i<=179):
        c_08 += case[i]
    elif(i<=209):
        c_09 += case[i]
    elif(i<=240):
        c_10 += case[i]
    elif(i<=270):
        c_11 += case[i]
    elif(i<=287):
        c_12 += case[i]

c_01 = 10
c_02 = 3140
c_03 += 5766-3150

month_case = [0,0,0,0,0]
month_case.append(c_01)
month_case.append(c_02)
month_case.append(c_03)
month_case.append(c_04)
month_case.append(c_05)
month_case.append(c_06)
month_case.append(c_07)
month_case.append(c_08)
month_case.append(c_09)
month_case.append(c_10)
month_case.append(c_11)
month_case.append(c_12)

result_ratio.append(0)
result_ratio.append(0)
result_ratio.append(0)
result_ratio.append(0)

colors = ['skyblue','lightskyblue','lightblue','powderblue','paleturquoise', 'peachpuff', 'lightsalmon','lightcoral', 'salmon', 'darksalmon', 'pink','coral', 'tomato','indianred','firebrick','brown','maroon']
result_title = ['~2019.08','2019.09','2019.10','2019.11','2019.12','2020.01','2020.02','2020.03','2020.04','2020.05','2020.06','2020.07','2020.08','2020.09','2020.10','2020.11','2020.12~']
plt.rcParams['figure.figsize'] = (18, 8)
fig, ax1 = plt.subplots()
ax1.bar(result_title, result_ratio, color=colors)
ax1.set_title('movie-COVID')
ax1.set_xlabel('Date')
ax1.set_ylabel('movie rate')
ax1.set_ylim(0,20)
ax2 = ax1.twinx()
ax2.plot(month_case, label='Number of confirmed cases per month', color='firebrick')
ax2.set_ylabel('number of people')
ax2.legend(loc='upper left')
ax2.set_ylim(0,12000)

plt.show()