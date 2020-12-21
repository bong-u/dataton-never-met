import requests
import bs4

def search(query):
    url = 'https://www.youtube.com/results'
    header = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    payload = {'search_query' : '족발'}
    
    res = requests.get(url, headers=header, params=payload)

    print(res)
    
    f = open('res.txt', 'w', -1, 'utf-8')
    f.write (res.text)
    

    print (res.text)
    
    #res = bs4.BeautifulSoup(res.text, "lxml")
    

search('족발')


