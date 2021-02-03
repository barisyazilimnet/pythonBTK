import requests
from bs4 import BeautifulSoup

url ="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find_all("li",{"class":"column"},limit =1)
for li in list:
    name = li.div.a.h3.text
    link = li.div.a.get("href")
    old_price = li.div.find("div",{"class":"proDetail"}).find("a",{"class":"oldPrice"})
    # new_price = li.div.find("div",{"class":"proDetail"}).find("a",{})
    print(name,"\n",link,"\n",old_price,"\n")



    ##### n11.com dan veri çekme