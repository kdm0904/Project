import bs4

html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
        <div>
            <ul>
                <li>open</li>
                <li>close</li>
            </ul>
        </div>    
    </body)
</html>
"""
#no 뽑기
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul", {"class" : "reply"})
lis = ul.findAll("li")

for li in lis[1:2]:
    print(li.text)