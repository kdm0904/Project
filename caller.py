from string_getter import getPageString
from bs4 import BeautifulSoup as bs
from youtubedata import gettitles
from youtubedata import getyoutubers
from youtubedata import getviews
from youtubedata import gettimes
import pandas as pd

keyword = "코팅제"

title = []
for word in keyword:
    url = "https://www.youtube.com/results?search_query="+word
    pageString = getPageString(url)
    output1 = gettitles(pageString)
    title = title + output1

youtuber = []
for word in keyword:
    url = "https://www.youtube.com/results?search_query="+word
    pageString = getPageString(url)
    output2 = getyoutubers(pageString)
    youtuber = youtuber + output2

view = []
for word in keyword:
    url = "https://www.youtube.com/results?search_query="+word
    pageString = getPageString(url)
    output3 = getviews(pageString)
    view = view + output3

time = []
for word in keyword:
    url = "https://www.youtube.com/results?search_query="+word
    pageString = getPageString(url)
    output4 = gettimes(pageString)
    time = time + output4

print(len(title), len(youtuber), len(view), len(time))

cdata = {'title':title, 'youtuber':youtuber, 'view':view, 'time':time}
df = pd.DataFrame(cdata)
df.to_csv("./coating_youtube.csv", sep = ',', encoding="UTF-8")