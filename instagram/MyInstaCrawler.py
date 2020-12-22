from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


email = input('email?')
pwd = input('passwd?')

BASE_URL = 'https://www.instagram.com/'
SEARCH_URL = BASE_URL + 'explore/tags/'

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get (BASE_URL)
sleep(1)

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
    sleep(2)

def crawl():

    first = driver.find_element_by_css_selector('div._9AhH0')
    first.click()
    sleep(1)
    
    for i in range(10):
        soup = BeautifulSoup(driver.page_source, 'lxml')

        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]

        print (date)
        
        right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
        right.click()
        sleep(0.5)
    
    


login()
search('치킨')
crawl()
