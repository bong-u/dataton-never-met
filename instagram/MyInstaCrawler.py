from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, time
from bs4 import BeautifulSoup


email = input('email?')
pwd = input('passwd?')

BASE_URL = 'https://www.instagram.com/'
SEARCH_URL = BASE_URL + 'explore/tags/'

options = webdriver.ChromeOptions()
options.add_argument('headless')
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

    first = driver.find_element_by_css_selector('div._9AhH0')
    first.click()
    sleep(1)

    with open('result.txt', 'w') as file:
    
        for i in range(100):
            soup = BeautifulSoup(driver.page_source, 'lxml')


            date = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'time._1o9PC.Nzb55'))).get_attribute("datetime")[:10]

            print (date)
            file.write(date + '\n')
        
            right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
            right.click()


start = time()
login()
search('치킨')
crawl()

print (time() - start)
