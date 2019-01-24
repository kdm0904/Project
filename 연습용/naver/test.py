from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = "https://news.naver.com/"
html = urlopen(url)
bs_obj = bs(html.read(), "html.parser")

ul = bs_obj.find("ul", {"id" : "text_today_main_news_428288"})
lis = ul.findAll("li")

titles = [li.find("strong").text for li in lis]

for title in titles:
    print(title)