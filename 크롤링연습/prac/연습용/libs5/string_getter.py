import requests 
from bs4 import BeautifulSoup as bs

def getPageString(url):
    data = requests.get(url)
    return data.content

