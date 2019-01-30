from bs4 import BeautifulSoup as bs

html = """
    <html>
        <table>
            <tr>
                <td class="first">100</td>
                <td>200</td>
            </tr>
            <tr>
                <td>300</td>
                <td>400</td>
            </tr>
        </table>
    </html>
"""

bs_obj = bs(html, "html.parser")

#100 찾기
td_first = bs_obj.find("td", {"class" : "first"})
# print(td_first.text)

#200 찾기
table = bs_obj.find("table")
tr = table.find("tr")
tds = tr.findAll("td")
print(tds[1].text)