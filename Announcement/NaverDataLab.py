import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('./datalab.xlsx',  usecols="A:D")
print(df)
sample = pd.pivot_table(df, values=['배달음식','음식','코로나'], index=["날짜"],aggfunc=np.mean)
print(sample)
sample1 = sample[['배달음식']]
sample2 = sample[['음식']]
sample3 = sample[['코로나']]
print(sample1)
print(sample2)
print(sample3)
plt.figure(figsize=(16,6))
plt.plot(sample1, label='delivery', color='cornflowerblue')
plt.plot(sample2, label='food', color='powderblue')
plt.plot(sample3, label='colona', color='plum')
plt.xlabel('date')
plt.ylabel('relative quantity')
plt.title("measured quantity")
tick_lab = ["2019-12-20", "2020-01-20", "2020-02-20", "2020-03-20", "2020-04-20", "2020-05-20", "2020-06-20", "2020-07-20", "2020-08-20", "2020-09-20", "2020-10-20", "2020-11-20", "2020-12-20"]
plt.xticks(tick_lab)
plt.legend()
plt.show()