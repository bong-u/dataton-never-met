import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
social = 2498 #3일간
yogiyo = 190 #2일간
house = 4018 #2일간
delivery = 323
baemin = 1074
delivery_2019= [30, 19, 25, 16, 21, 12, 26, 14, 51, 23,17, 24]
delivery_2020 = [17, 26, 45, 62, 68, 78, 88, 107, 111, 89, 133, 246]
relate = []
relate.append(social)
relate.append(baemin)
relate.append(yogiyo)
relate.append(house)


label1 = ['01','02','03','04','05','06','07','08','09','10','11','12']
label2 = ['Social distancing','Baemin','Yogiyo','Zipcock']
x = np.arange(len(label1))
plt.rcParams['figure.figsize'] = (18, 8)
plt.subplot(121)
plt.bar(x-0.0,delivery_2019,label='delivery_food_store_2019',width=0.2,color='lightskyblue')
plt.bar(x+0.2,delivery_2020,label='delivery_food_store_2020',width=0.2,color='royalblue')
plt.xticks(x,label1)
plt.legend()
plt.xlabel('Date')
plt.ylabel('Posting count')
plt.ylim(0,270)
plt.title('food_COVID')

plt.subplot(122)
x = np.arange(len(label2))
plt.ylabel('Posting count')
plt.xticks(x,label2)
colors = ['salmon', 'darksalmon', 'pink','tomato']
plt.bar(x,relate,width=0.5,color=colors)
plt.title('relate_COVID')

plt.suptitle('Instargram')

plt.show()