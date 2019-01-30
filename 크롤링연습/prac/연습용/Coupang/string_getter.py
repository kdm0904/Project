import requests 
from bs4 import BeautifulSoup as bs

def getPageString(url):
    data = requests.get(url)
    print(data.status_code)
    return data.content

