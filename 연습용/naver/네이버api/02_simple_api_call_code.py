import requests
from urllib.parse import urlparse

keyword = "디퓨져"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(), 
                      headers = {"X-Naver-Client-Id" : "8BZuX_sDay6FsOoGnqzo",
                                "X-Naver-Client-Secret" : "WcFE1BMkZx"})
json_obj = result.json()
print(json_obj)