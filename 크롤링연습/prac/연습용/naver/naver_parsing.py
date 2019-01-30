import urllib.request
from bs4 import BeautifulSoup as bs
url = "https://www.naver.com"
html = urllib.request.urlopen(url)
bsObj = bs(html, "html.parser")

#print(html.read())
#print(bsObj)

top_right = bsObj.find("div", {"class":"area_links"})
first_a = top_right.find("a")

print(first_a.text)