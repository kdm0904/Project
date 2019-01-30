from string_getter import getPageString
from bs4 import BeautifulSoup as bs
from products_parser import getProducts

url = "https://www.coupang.com/np/categories/186764?page=2"
pageString = getPageString(url)
products = getProducts(pageString)

for product in products:
    print(product)