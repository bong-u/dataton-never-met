from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass


email = getpass('id : ')
pwd = getpass('passwd : ')
query = input('query : ')

BASE_URL = 'https://www.instagram.com/'
SEARCH_URL = BASE_URL + 'explore/tags/'

options = webdriver.ChromeOptions()
#options.add_argument('headless')               #headless 모드 -> 크롬 창 안 띄우는 것
options.add_argument('window-size=1920x1080')   #창 크기 지정
options.add_argument("disable-gpu")             #빠른 크롤링을 위한 최적화 
options.add_argument("disable-infobars")        #빠른 크롤링을 위한 최적화 
options.add_argument("--disable-extensions")    #빠른 크롤링을 위한 최적화 
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")         #uger-agent
options.add_experimental_option("excludeSwitches", ["enable-logging"])      #장치가 없다는 경고 안 뜨게 함.
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get (BASE_URL)           #인스타그램 접속
sleep(3)

def login():
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]      #아이디 입력 박스 선택 
    input_id.clear()                                                                    #비움
    input_id.send_keys(email)                                                           #아이디 전송
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]      #비밀번호 입력박스 선택 
    input_pw.clear()
    input_pw.send_keys(pwd)                                                             #비밀번호 전송
    input_pw.submit()                                                                   #로그인
    sleep(2)                                                                            #로딩

def search(query):
    driver.get(SEARCH_URL + query)                                                      #query를 검색한 사이트로 이동
    sleep(2.5)                                                                          #로딩

def crawl():

    srcList = []                                                                        #중복 방지 리스트

    open('result.txt', 'w')                                                             #출력 파일 비우기
    
    for i in range(30000):                                                              #대충 스크롤 30000번 하겠다는 뜻
        imgList = driver.find_elements_by_css_selector('img.FFVAD')                     #find img by selector
        
        dateList = ''

        for j in range(len(imgList)):
            alt = str(imgList[j].get_attribute('alt'))                                  #날짜가 포함된 alt
            src = str(imgList[j].get_attribute('src'))                                  #중복을 방지하기 위한 src

            if src in srcList:                                                          #중복되는게 있으면 pass
                continue

            if not alt.startswith('Photo by'):                                          #사진에 날짜가 없으면 pass (이런경우 잘 없음)
                continue

            if ' on ' not in alt:                                                       #사진에 날짜가 없으면 pass (이런경우 잘 없음)
                continue

            date = alt.split(' on ')[1].split('.')[0]                                   #날짜 부분만 추출
            print(date)                                                                 #날짜 출력
            dateList += date + '\n'                                                     #dateList에 추가
            srcList.append(src)                                                         #중복방지 리스트에 추가


        with open('result.txt', 'a') as f:                                              #파일에 기록
            f.write(dateList)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        #스크롤

        sleep(1.0)                                                                      #로딩 기다려주기



start = time()                                                                          #시간 측정 시작

login()                                                                                 #로그인
search(query)                                                                           #검색
crawl()                                                                                 #크롤링

print (time() - start)                                                                  #측정된 시간 출

