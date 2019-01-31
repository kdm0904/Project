from bs4 import BeautifulSoup as bs

def gettitle(div):
    title2 = div.find("div", {"id" : "title-wrapper"})
    title1 = title2.find("h3", {"class":"title-and-badge style-scope ytd-video-renderer"})
    title = title1.find("a", {"id":"video-title"})
    return title.text

def getyoutuber(div):
    Youtuber1 = div.find("div", {"id":"byline-inner-container"})
    Youtuber = Youtuber1.find("a", {"class":"yt-simple-endpoint style-scope yt-formatted-string"})
    return Youtuber.text

def getview(div):
    view1 = div.find("div", {"id":"metadata-line"})
    view = view1.find("span", {"class":"style-scope ytd-video-meta-block"})
    return view.text

def gettime(div):
    time = div.findAll("span", {"class":"style-scope ytd-video-meta-block"})
    return time[1].text

def gettitles(string):
    bsObj = bs(string, "html.parser")
    
    contents = bsObj.find("div", {"id" : "contents"})
    divs = contents.findAll("div")

    title = []

    for div in divs:
        title.append(gettitle(div))
    return title

def getyoutubers(string):
    bsObj = bs(string, "html.parser")
    
    contents = bsObj.find("div", {"id" : "contents"})
    divs = contents.findAll("div")

    youtuber = []

    for div in divs:
        youtuber.append(getyoutuber(div))
    return youtuber

def getviews(string):
    bsObj = bs(string, "html.parser")
    
    contents = bsObj.find("div", {"id" : "contents"})
    divs = contents.findAll("div")

    view = []

    for div in divs:
        view.append(getview(div))
    return view

def gettimes(string):
    bsObj = bs(string, "html.parser")
    
    contents = bsObj.find("div", {"id" : "contents"})
    divs = contents.findAll("div")

    time = []

    for div in divs:
        time.append(gettime(div))
    return time

