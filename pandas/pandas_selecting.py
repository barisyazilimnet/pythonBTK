import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])
result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]
result = df.loc["A"]
result = type(df.loc["A"])

# loc["A","Column1"]
# loc["A"]
# loca[:,"Column1"]

result = df.loc[:, "Column1"]
result = df.loc[:, ["Column1","Column2"]]
result = df.loc[:, "Column1":"Column3"] ## başlangıç ve bitiş dahil olmak üzere arasındaki columnları verir
result = df.loc[:, :"Column3"] ## başlangıçdan itibaren bitiş dahil olmak üzere arasındaki columnları verir
result = df.iloc[2] ## ikinci indexdeki degerleri verir
result = df.loc["A","Column2"] ## A indexindeki Column2 sütunundaki degeri verir

df["Column4"] = pd.Series(randn(3), ["A","B","C"]) ## 4. sütunu ekler
df["Column5"] = df["Column1"] + df["Column3"] ## 5. sütunu ekler ama 5. sütun 1 ve 3. sütunların toplamıdır
print(df.drop("Column5", axis = 1)) ## 5. sütunu siler  ## inplace = True parametresi yazıldıgı takdirde orjinalinde de güncelleme yapar 
print(df)
# print(result)