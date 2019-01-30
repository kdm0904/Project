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
    
    
    # close 종가(전일)
    close = blind.text
    
    # high 고가
    table = bs_obj.find("table", {"class" : "no_info"})
    trs = table.findAll("tr")
    first_tr = trs[0]
    first_tr_tds = first_tr.findAll("td")
    first_tr_tds_second_td = first_tr_tds[1]
    high = first_tr_tds_second_td.find("span", {"class" : "blind"}).text 

    # open 시가
    second_tr = trs[1]
    second_tr_td_first = second_tr.find("td", {"class" : "first"})
    blind_open = second_tr_td_first.find("span", {"class" : "blind"})
    open = blind_open.text

    # low 저가
    second_tr_tds = second_tr.findAll("td")
    second_tr_second_td = second_tr_tds[1]
    blind_low = second_tr_second_td.find("span", {"class" : "blind"})
    low = blind_low.text

    return {"close" : close, "high" : high, "open" : open, "low" : low}


    

candle_chart_data = get_candle_chart_data("000660")
print(candle_chart_data)
