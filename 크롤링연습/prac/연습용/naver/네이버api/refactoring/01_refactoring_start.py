import requests
from bs4 import BeautifulSoup as bs

#url 넣어 bs_obj를 return하는 function 제작

url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
bs_obj = bs(result.content, "html.parser")
print(bs_obj)