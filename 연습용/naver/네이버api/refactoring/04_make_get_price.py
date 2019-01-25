import requests
from bs4 import BeautifulSoup as bs

#url 넣어 bs_obj를 return하는 function 제작
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = bs(result.content, "html.parser")
    return bs_obj

#companycode를 받아서 가격을 return하는 함수
def get_price (company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    bs_obj = get_bs_obj(url)
    no_today = bs_obj.find("p", {"class" : "no_today"})
    blind = no_today.find("span", {"class" : "blind"})
    return blind.text

price_samsung = get_price("005930")
price_skhynix = get_price("000660")
print (price_samsung)
print (price_skhynix)

