import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

result_ratio = [8.22, 6.13, 4.41, 11.64, 5.72, 5.17, 2.65, 0, 0.22, 0.08, 3.25, 5.81, 5.33,0,0,0,0]
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