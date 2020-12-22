import requests

HEADER = {
    'User-agent' : 'Mozilla/5.0'
    }


LOGIN_INFO = {
    'userid' : 'thsqhddn7',
    'password' : 'sbw201379',
    'redirect' : '/'
    }

SEARCH_URL = 'https://everytime.kr/search/all/'
LOGIN_URL = 'https://cnu.everytime.kr/user/login'
API_URL = 'https://api.everytime.kr/search/all'

with requests.Session() as s:
    res = s.get(LOGIN_URL, headers=HEADER, data = LOGIN_INFO)
    if res.status_code != 200:
        raise Exception('Login Failed!')

    print (res)
    
    res = s.get(API_URL + '음식', headers=HEADER)

    print (res)

    print(res.text)
    

'''
with open("everytime.txt", 'w') as f:
    f.write(res.text)
'''
