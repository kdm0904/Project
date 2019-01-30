from bs4 import BeautifulSoup as bs

def getProduct(li):
    img = li.find("dt", {"class" : "image"}).find("img")
    return img['alt']

def productprice(li):
    priceWrap = li.find("div", {"class":"price-wrap"})
    strong = priceWrap.find("strong")
    return strong.text

def getProducts(string):
    bsObj = bs(string, "html.parser")
    
    ul = bsObj.find("ul", {"id" : "productList"})
    lis = ul.findAll("li")
    
    productsname = []

    for li in lis:
        productsname.append(getProduct(li))
    return productsname

def getProductsprice(string):
    bsObj = bs(string, "html.parser")
    
    ul = bsObj.find("ul", {"id" : "productList"})
    lis = ul.findAll("li")

    productsprice = []

    for li in lis:
        productsprice.append(productprice(li))
    return productsprice