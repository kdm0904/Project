from string_getter import getPageString
from bs4 import BeautifulSoup as bs
from products_parser import getProducts

categoryProducts = []
for pageNum in range(1, 2):
    url = "https://www.coupang.com/np/categories/186764?page={}".format(pageNum)
    pageString = getPageString(url)
    products = getProducts(pageString)
    categoryProducts = categoryProducts + products

print(len(categoryProducts)) 
for product in categoryProducts:
    print(product)

