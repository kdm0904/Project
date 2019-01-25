import requests
from bs4 import BeautifulSoup as bs

#url 넣어 bs_obj를 return하는 function 제작
def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = bs(result.content, "html.parser")
    return bs_obj

#companycode를 받아서 가격을 return하는 함수
def get_candle_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)
    td_first = bs_obj.find("td", {"class" : "first"})
    blind = td_first.find("span", {"class": "blind"})
    #close 종가(전일)
    close = blind.text
    return close
    

candle_chart_data = get_candle_chart_data("000660")
print(candle_chart_data)


