from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_bb130305787cf2c7317a29135dc3c314")

soup = BeautifulSoup(html, 'lxml')



table = soup.find("svg")
g = table.g


