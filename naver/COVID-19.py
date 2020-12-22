import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('./total_corona_count.xlsx',  usecols="A:F")
print(df)

sample = pd.pivot_table(df, values=['일일확진자수','누적사망자수'], index=["날짜"],aggfunc=np.mean)
print(sample)
sample1 = sample[['일일확진자수']]
sample2 = sample[['누적사망자수']]
print(sample1)
print(sample2)
plt.figure(figsize=(16,6))
plt.title("COVID-19")
plt.xlabel('date')
plt.ylabel('quantity')
plt.xticks([20200310,20200410,20200510,20200610,20200710,20200810,20200910,20201010,20201110,20201210])
plt.plot(sample2, label='Cumulative number of confirmed cases', color='powderblue')
plt.plot(sample1, label='Number of confirmed cases per day', color='tomato')
plt.legend()
plt.show()


