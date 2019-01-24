from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = "https://news.naver.com/"
html = urlopen(url)
bs_obj = bs(html.read(), "html.parser")

ul = bs_obj.find("ul", {"id" : "text_today_main_news_428288"})
lis = ul.findAll("li")

for li in lis :
    newsnow = li.find("div", {"class" : "newsnow_tx_inner"})
    block = newsnow.find ("a", {"class": "nclicks(hom.headcont)"})
    title = block.find("strong")
    print(title.text)

