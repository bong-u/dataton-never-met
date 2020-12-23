import matplotlib.pyplot as plt
from wordcloud import WordCloud

font_path = 'c:\\windows\\fonts\\NanumGothic.ttf'
wordcloud = WordCloud(font_path = font_path,width = 800,height = 800,background_color='white')
text=open('hashtag-음식.txt').read()
wordcloud = wordcloud.generate(text)

fig = plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis("off")


text=open('hashtag-코로나.txt').read()
wordcloud = wordcloud.generate(text)
fig = plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis("off")

text=open('hashtag-취미2.txt').read()
wordcloud = wordcloud.generate(text)
fig = plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()

