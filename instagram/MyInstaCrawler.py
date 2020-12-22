import requests
import bs4
import json

'''
def auth():
    query = '치킨'
    
    session = requests.Session()
    session.cookies.set('ig_pr', '1')
    session.headers = {'Referer' : 'https://www.instagram.com/',
                       'user-agent' : 'Instagram 123.0.0.21.114 (iPhone; CPU iPhone OS 11_4 like Mac OS X; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/605.1.15' }

    req = session.get('https://www.instagram.com/')

    session.headers.update({'X-CSRFToken' : req.cookies['csrftoken']})
    session.headers.update({'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'})

    res = session.get('https://www.instagram.com/explore/tags/%s' % query)

    print(res)
    print(res.text)
'''
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

def search(query):
    url = 'https://www.instagram.com/graphql/query/?query_hash=f92f56d47dc7a55b606908374b43a314&variables= {"tag_name": "%s", "first": 10}' % query
    header = {'User-agent' : USER_AGENT}
    
    res = requests.get(url, headers = header)

    print(res)
    
    #f = open('res.txt', 'w', -1, 'utf-8')
    #.write (res.text)

    #dict = json.loads(res.text)

    print (res.text)
    
    #res = bs4.BeautifulSoup(res.text, "lxml")
    
search ('족발')


