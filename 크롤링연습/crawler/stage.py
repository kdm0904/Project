from naver_api_caller import get1000Result
import json

list = []
result = get1000Result("코팅제")
list = list + result

print(len(list))

file = open("./coating.json", "w+")
file.write(json.dumps(list))
json.dumps(list)