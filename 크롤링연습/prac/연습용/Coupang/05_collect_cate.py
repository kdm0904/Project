from string_getter import getPageString
from bs4 import BeautifulSoup as bs
from pp import getProducts
from pp import getProductsprice
import pandas as pd

name = []
for pageNum in range(1, 6):
    url = "https://www.coupang.com/np/categories/186764?page={}".format(pageNum)
    pageString = getPageString(url)
    products = getProducts(pageString)
    name = name + products

price = []
for pageNum in range(1, 6):
    url = "https://www.coupang.com/np/categories/186764?page={}".format(pageNum)
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

df.to_csv("./femaleclothes.csv", sep = ',', encoding="UTF-8")

