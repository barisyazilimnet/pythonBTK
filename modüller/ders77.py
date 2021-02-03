html_doc ="""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Barış KURT</title>
    </head>
    <body>
        <h1>Python Kursu</h1>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
        <div class="group_1">
            <h2>Programlama</h2>
            <ul>
                <li>Menü 1</li>
                <li>Menü 2</li>
                <li>Menü 3</li>
            </ul>
        </div>
        <div class="group_2">
            <h2>Modüller</h2>
            <ul>
                <li>Menü 1</li>
                <li>Menü 2</li>
                <li>Menü 3</li>
            </ul>
        </div>
        <div class="group_3">
            <h2>Django</h2>
            <ul>
                <li>Menü 1</li>
                <li>Menü 2</li>
                <li>Menü 3</li>
            </ul>
        </div>
        <img src="https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80" alt="resim">
        <a href="https://kurtbaris.com">Barış KURT</a>
        <a href="https://kurtbaris1.com">Barış KURT1</a>
        <a href="https://kurtbaris2.com">Barış KURT2</a>
    </body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")
result = soup.prettify()    #html kodunu düzenlenmiş kod düzeni halinde gösterir
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name
result = soup.title.string
result = soup.h1
result = soup.h2 # sadece ilk h2 getirir
result = soup.h2.name
result = soup.h2.string
result = soup.h1.string
result = soup.find_all("h2") #bütün h2 leri getirir
result = soup.find_all("h2")[0] #ilk h2 getirir
result = soup.find_all("h2")[1] #ikinci h2 getirir
result = soup.div
result = soup.find_all("div")
result = soup.find_all("div")[1]
result = soup.find_all("div")[1].ul #ikinci divin altındaki ul etiketini getirir
result = soup.find_all("div")[1].ul.li #ikinci divin altındaki ul etiketinin ilk li sini getirir
result = soup.find_all("div")[1].ul.find_all("li") #ikinci divin altındaki ul etiketinin bütün li sini getirir

result = soup.div.findChildren() # div altındaki etiketler getiriliyor
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling() # her bir findNextSibling() methodu bir sonraki etikete geçirir  # her bir .findPreviousSibling() methodu da bir önceki etikete geçer
result = soup.find_all("a")
# for link in result:
#     print(link)
for link in result:
    print(link.get("href"))
# print(result)