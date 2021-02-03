import pandas as pd

data = pd.read_csv("nba.csv")
data.dropna(inplace = True)
# data["Name"] = data["Name"].str.upper() ## name kolonundaki bütün isimleri büyük harf yapar
# data["Name"] = data["Name"].str.lower() ## name kolonundaki bütün isimleri küçük harf yapar
# data["index"] = data["Name"].str.find("a") ## name kolonundaki a bulunan isimlerdeki a harfleri kaçıncı indexdeyse yeni index kolonu oluşturarak ora yazar
# data = data[data["Name"].str.contains("Jordan")] ## name kolonunda içerisinde jordan geçen isimleri bulur
# data = data["Team"].str.replace(" ","-")
data[["First_name","Last_name"]] = data["Name"].loc[data["Name"].str.split().str.len() == 2].str.split(expand = True) ## datanın name kolonundaki 1 li olan isimleri first_name ve last_name olmak üzere iki kolona böler
print(data.head())