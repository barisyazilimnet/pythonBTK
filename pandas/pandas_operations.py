import pandas as pd
import numpy as np

data = {
    "Column1" : [1,2,3,4,5],
    "Column2" : [10,20,13,45,25],
    "Column3" : ["ab","bca","ad","cb","deaa"]
}

df = pd.DataFrame(data)
result = df
result = df["Column2"].unique() ## tekrarlayan elemaları bir kere gösterir
result = df["Column2"].nunique() ## tek elemanlardan kaç tane var onu gösterir tekrarlayan elemanlarıda 1 kere sayar
result = df["Column2"].value_counts() ## her elemandan kaç tane oldugunu söler
result = df["Column1"] * 2 ## bütün elemanları ikiyle çarpar

def kare_al(x):
    return x * x

result = df["Column1"].apply(kare_al) ## bütün elemaları teker teker fonksiyona göndererek karesini hesaplar
result = df["Column1"].apply(lambda x: x * x) ## bütün elemanların tek tek karesini alır
result = df["Column3"].apply(len) ## bütün string ifadelerin kaç karakter oldgunu söler
result = df.columns ## kolonların isimlerini gösterir
result = len(df.columns) ## kolonların sayısını gösterir
result = df.index ## index hakkında bilgiler verir step == artış miktarı
result = len(df.index) ## kaç satır oldugunu gösterir
result = df.sort_values("Column2") ## küçükten büyüge göre sıralama yapar
result = df.sort_values("Column3") ## a dan z ye göre sıralama yapar
result = df.sort_values("Column3", ascending = False) ## z den a ya göre sıralama yapar

data = {
    "Ay" : ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori" : ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir" : [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
df = df.pivot_table(index = "Ay", columns = "Kategori", values = "Gelir")
print(df)
