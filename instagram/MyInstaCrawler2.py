from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, time
from bs4 import BeautifulSoup
from getpass import getpass


email = getpass('id : ')
pwd = getpass('passwd : ')
query = input('query : ')

BASE_URL = 'https://www.instagram.com/'
SEARCH_URL = BASE_URL + 'explore/tags/'

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu") 
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get (BASE_URL)
sleep(3)

def login():
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(email)
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(pwd)
    input_pw.submit()
    sleep(2)

def search(query):
    driver.get(SEARCH_URL + query)
    sleep(2.5)

def crawl():

    dateList = ''
    srcList = []
    
    for i in range(50):
        '''
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'img.FFVAD')))
        '''
        
        imgList = driver.find_elements_by_css_selector('img.FFVAD')

        for j in range(len(imgList)):
            alt = str(imgList[j].get_attribute('alt'))
            src = str(imgList[j].get_attribute('src'))

            if src in srcList:
                continue

            if not alt.startswith('Photo by'):
                continue

            if ' on ' not in alt:
                continue

            #date = alt.split(' on ')[1]
            date = alt.split(' on ')[1].split('.')[0]
            print(date)
            dateList += date + '\n'
            srcList.append(src)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(1.0)

    f = open('result.txt', 'w')
    f.write(dateList)


start = time()

login()
search(query)
crawl()
driver.close()

print (time() - start)
