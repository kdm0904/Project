import requests
from urllib.parse import quote

def get1000Result(keyword):
    list = []
    for num in range (1, 11):
        list = list + call("코팅제", num*100+1)['items']
    return list

def call (keyword, start): 
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText +\
          "&display=100" + "&start"+str(start) 
    result = requests.get(url=url, 
        headers = {"X-Naver-Client-Id" : "8BZuX_sDay6FsOoGnqzo",
                   "X-Naver-Client-Secret" : "WcFE1BMkZx"})
    print(result) # Response [401]
    return result.json()