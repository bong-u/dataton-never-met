from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, time
from getpass import getpass
import re


email = getpass('id?')
pwd = getpass('passwd?')
query = input('query?')

BASE_URL = 'https://www.instagram.com/'
SEARCH_URL = BASE_URL + 'explore/tags/'

options = webdriver.ChromeOptions()
#options.add_argument('headless')               #headless 모드 -> 크롬 창 안 띄우는 것
options.add_argument('window-size=1920x1080')   #창 크기 지정
options.add_argument("disable-gpu")             #빠른 크롤링을 위한 최적화 
options.add_argument("disable-infobars")        #빠른 크롤링을 위한 최적화 
options.add_argument("--disable-extensions")    #빠른 크롤링을 위한 최적화 
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")        #user-agent
options.add_experimental_option("excludeSwitches", ["enable-logging"])      #장치가 없다는 경고 안 뜨게 함.
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get (BASE_URL)           #인스타그램 접속
sleep(3)

def login():
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]      #아이디 입력 박스 선택
    input_id.clear()                                                                    #비움
    input_id.send_keys(email)                                                           #아이디 전송
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]      #비밀번호 입력 박스 선택
    input_pw.clear()                                                                    #비움
    input_pw.send_keys(pwd)                                                             #비밀번호 전송
    input_pw.submit()                                                                   #로그인
    sleep(2)                                                                            #로딩

def search(query):
    driver.get(SEARCH_URL + query)                                                      #query를 검색한 사이트로 이동

def crawl():

    open('hashtag.txt', 'w')                                                            #출력 파일 비우기

    first = WebDriverWait(driver, 5).until(                                             #첫번째 사진 요소가 로딩될 때 까지 기다림 -> 선택
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'div._9AhH0')))   
    first.click()                                                                       #클릭
    sleep(1)                                                                            #로딩


    for i in range(5000):                                                               #계속 반복

        line = ''
        for j in range(10):                                                             #10번할때마다 기록하기 위함

            content = WebDriverWait(driver, 5).until(                                   #게시물은 본문이 로딩될 때 까지 기다림 -> 선택
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '.C7I1f'))).text

            tags = re.findall('#[A-Za-z0-9가-힣]+', content)                              # (#+~~~~)로 된 형태를 추출

            for tag in tags:                                                            #해시태그를 돌며
                line += tag.replace ("#", "") + ' '                                     #공백과 함께 라인에 추가
        
            right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')        #다음 게시물 버튼 선택
            right.click()                                                               #다음 게시물 버튼 클릭

        date = WebDriverWait(driver, 5).until(                                          #시간 요소 선택
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'time'))).get_attribute("datetime")

        print(date)                                                                     #날짜 출력
        print (line)                                                                    #해시태그 출력

        with open("hashtag.txt", 'a') as f:                                             #출력 파일에 추가
            f.write(line)                                                               #해시태그를 파일에 작성
            f.write('\n' + date + '\n')                                                 #날짜를 파일에 작성


start = time()                                                                          #시간 측정 시작

login()                                                                                 #로그인
search(query)                                                                           #검색
crawl()                                                                                 #크롤링

print (time() - start)                                                                  #측정된 시간 출
