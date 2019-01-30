from bs4 import BeautifulSoup
html_str = "<html><div></div></html>"
bsObj = BeautifulSoup(html_str, "html.parser") 

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))
