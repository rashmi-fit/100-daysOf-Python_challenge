import requests
from bs4 import BeautifulSoup


def extract(page):
    url=f'https://uk.indeed.com/jobs?q=python%20developer&l=London&start={page}'
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    r= requests.get(url,headers = headers)
    print(r.status_code)

    soup=BeautifulSoup(r.content,'html.parser')
    return soup



c = extract(0)


