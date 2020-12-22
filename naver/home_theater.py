import matplotlib.pyplot as plt
import numpy as np

Home_theater = [72 ,88 ,98 ,100 ,96, 112, 159, 143, 113, 115, 127] #9월부터 7월

label = ['19.09','19.10','19.11','19.12',
         '20.01', '20.02', '20.03', '20.04', '20.05', '20.06', '20.07']

x = np.arange(len(label))

plt.rcParams['figure.figsize'] = (12, 8)
plt.bar(x,Home_theater,width=0.4,color='lavender')
plt.plot(Home_theater,color='slateblue',marker='o')
plt.xticks(x,label)
plt.xlabel('Month')
plt.ylabel('Posting count')
plt.ylim(0,170)
plt.title('Home theater')
plt.show()