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
    </body)
</html>
"""
# bye 뽑기
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
lis = bs_obj.findAll("li")
print(lis)

for li in lis:
    print(li)