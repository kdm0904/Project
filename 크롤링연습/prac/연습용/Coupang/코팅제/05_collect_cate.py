from string_getter import getPageString
from bs4 import BeautifulSoup as bs
from pp import getProducts
from pp import getProductsprice
import pandas as pd

name = []
for pageNum in range(1, 11):
    url = "https://www.coupang.com/np/search?q=%EC%85%80%ED%94%84%EC%8B%9C%EA%B3%B5+%EC%BD%94%ED%8C%85%EC%A0%9C&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false".format(pageNum)
    pageString = getPageString(url)
    products = getProducts(pageString)
    name = name + products

price = []
for pageNum in range(1, 11):
    url = "https://www.coupang.com/np/search?q=%EC%85%80%ED%94%84%EC%8B%9C%EA%B3%B5+%EC%BD%94%ED%8C%85%EC%A0%9C&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false".format(pageNum)
    pageString = getPageString(url)
    pri = getProductsprice(pageString)
    price = price + pri

print(len(name), len(price)) 
for product in name:
    print(product)

for productprice in price:
    print(productprice)

cdata = {'name':name, 'price':price}
df = pd.DataFrame(cdata)

df.to_csv("./self_coating.csv", sep = ',', encoding="UTF-8")

