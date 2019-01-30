from string_getter import getPageString
from bs4 import BeautifulSoup as bs

def getProducts(string):
    bsObj = bs(string, "html.parser")
    
    ul = bsObj.find("ul", {"id" : "productList"})
    lis = ul.findAll("li")
    li = lis[0]
    print(li)
    return []

url = "https://www.coupang.com/np/categories/186764?page=1"
pageString = getPageString(url)
print(getProducts(pageString))
