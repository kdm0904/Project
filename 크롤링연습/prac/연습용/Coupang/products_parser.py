from bs4 import BeautifulSoup as bs

def getProduct(li):
    img = li.find("dt", {"class" : "image"}).find("img")
    priceWrap = li.find("div", {"class":"price-wrap"})
    strong = priceWrap.find("strong")
    return{"name":img['alt'], "price":strong.text}

def getProducts(string):
    bsObj = bs(string, "html.parser")
    
    ul = bsObj.find("ul", {"id" : "productList"})
    lis = ul.findAll("li")
    
    products = []
    
    for li in lis:
        products.append(getProduct(li))
    return products
