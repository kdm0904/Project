import requests
from bs4 import BeautifulSoup as bs

def crawl(url):
    result = requests.get(url)
    bs_obj = bs(result.content, "html.parser")
    return bs_obj