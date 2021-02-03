import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Columns1","Columns2","Columns3","Columns4","Columns5"])

result = df
result = df.columns ## sütunların isimlerini verir
result = df.head() ## ilk 5 satırı verir
result = df.head(10) ## ilk 10 satırı verir
result = df.tail() ## son 5 satırı verir
result = df.tail(10) ## son 10 satırı verir
result = df["Columns1"].head() ## Columns1 sütunun ilk 5 satırını verir
result = df[["Columns1","Columns3"]].head()
result = df[["Columns1","Columns3"]].tail()
result = df[5:15][["Columns1","Columns3"]].head()
result = df > 50 ## dataframe de degerlere bakar 50 den büyük olanlar true
result = df[df > 50]
result = df["Columns1"] > 50 ## sadece ilk sütundaki 50 den büyük olan degerlere true
result = df[df["Columns1"] > 50]["Columns1"]
result = df[(df["Columns1"] > 50) & (df["Columns1"] <= 70)]["Columns1"]
result = df[(df["Columns1"] > 50) & (df["Columns2"] <= 70)][["Columns1","Columns2"]]
result = df.query("Columns1 > 50 | Columns1 %2 == 0")["Columns1"]
print(result)