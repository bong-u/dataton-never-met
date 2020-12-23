import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

delivery = [51, 23, 17, 24, 17, 26, 45, 62, 68, 78, 88, 107, 111, 89, 133, 246]
review = [16, 69, 48, 56, 68, 152, 122, 189, 279, 214, 262, 224, 424, 295, 342, 314]
social = 2498 #3일간
yogiyo = 190 #2일간
house = 4018 #2일간

label = ['19.09','19.10','19.11','19.12',
         '20.01', '20.02', '20.03', '20.04', '20.05', '20.06', '20.07', '20.08', '20.09', '20.10', '20.11', '20.12' ]
x = np.arange(len(label))

plt.rcParams['figure.figsize'] = (12, 8)
plt.bar(x-0.0,review,label='delivery_food_review',width=0.2,color='mediumpurple')
plt.bar(x+0.2,delivery,label='delivery_food_store',width=0.2,color='gold')
plt.xticks(x,label)

plt.legend()
plt.xlabel('Date')
plt.ylabel('Posting count')
plt.ylim(0,450)
plt.title('food_COVID')
plt.show()