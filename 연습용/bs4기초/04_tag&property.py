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

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
# tag 태그 <ul></ul> <li></li> <div></div> <a>
# property 속성 id, class, href, title 
# property value 속성값 class ="greet"에서 greet이 속성값
# <a href= "www.google.com">구글</a> 태그와 속성값은? :
# tag = a, property = href, property_value of href= www.google.com
# html <html></html>

# ok no sure 뽑기
ul_reply =  bs_obj.find("ul", {"class" : "reply"})
print(ul_reply)