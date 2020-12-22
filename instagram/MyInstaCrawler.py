from selenium import webdriver
from time import sleep


email = input('email?')
pwd = input('passwd?')

BASE_URL = 'https://www.instagram.com/'
SEARCH_URL = BASE_URL + 'explore/tags/'

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get (BASE_URL)
sleep(2)

def login():
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(email)
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(pwd)
    input_pw.submit()
    sleep(5)

def search():
    drvier.get(SEARCH_URL)



login()
search('치킨')
