import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index = ["a","c","e","f","h"], columns = ["Columns1","Columns2","Columns3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])
new_columns = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]
df["Columns4"] = new_columns

result = df
result = df.drop("Columns1", axis = 1) ## kolon 1 sütun olarak siler
result = df.drop(["Columns1","Columns2"], axis = 1)
result = df.drop("a", axis = 0) ## a satırını siler
result = df.isnull() ## boş olan olanlar true olarak gelir
result = df.notnull() ## deger yazılı olan yerler true olarak gelecektir
result = df.isnull().sum() ## her kolonda kaç tane boş deger var sayar
result = df["Columns1"].isnull().sum() ## kolon 1 deki boş degerleri sayar
result = df[df["Columns1"].isnull()]["Columns1"] ## kolon 1 deki boş alanları getirir
result = df.dropna() # axis = 0  ## satırda boş alan varsa o satırı sil
result = df.dropna(axis = 1) ## sütunda boş alan varsa o sütunu sil
result = df.dropna(how = "any") ## kolonda boş olan degeri sil
result = df.dropna(how = "all") ## kolondaki bütün boş degerli sil
result = df.dropna(subset = ["Columns1","Columns2"]) ## sadece kolon 1 ve kolon 2 yi kontrol eder
result = df.dropna(thresh = 2) ## bir satırda en az 2 tanede deger varsa silme
result = df.fillna(value = "Boş") ## boş olan degerler yerine boş yazar
result = df.sum() ## kolonları toplar
result = df.sum().sum() ## dataframe deki bütün verileri toplar
result = df.size ## dataframe deki veri sayısını verir
result = df.isnull().sum() ## kolonlardaki boş alanların toplam sayısını verir
result = df.isnull().sum().sum() ## bütün dataframe deki boş alanların toplam sayısını verir
print(result)