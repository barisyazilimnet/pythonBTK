import pandas as pd
import numpy as np

# # data
# numbers = [20,30,40,50]
# numbers = np.array([20,30,40,50])
# letters = ["a","b","c","d"]
# letters_number = ["a","b","c","d",20]
# scalar = 5
# dict = {"a":10, "b":20, "c":30, "d":40}
# random_numbers = np.random.randint(10,100,6)

# # pandas_series = pd.Series()
# # pandas_series = pd.Series(numbers)
# # pandas_series = pd.Series(letters)
# # pandas_series = pd.Series(letters_number)
# # pandas_series = pd.Series(scalar)
# # pandas_series = pd.Series(scalar, [0,1,2,3])
# # pandas_series = pd.Series(5, [0,1,2,3])
# # pandas_series = pd.Series(numbers, ["a","b","c","d"]) ## numbers listesindeki kadar harf olmalı
# # pandas_series = pd.Series(dict)
# # pandas_series = pd.Series(random_numbers)
# pandas_series = pd.Series([20,30,40,50], ["a","b","c","d"])

# # result = pandas_series[0]
# # result = pandas_series[-1]
# # result = pandas_series[:2] ## ilk 2 eleman
# # result = pandas_series[-2:] ## son 2 eleman
# # result = pandas_series["a"] 
# # result = pandas_series["d"] 
# # result = pandas_series[["a","c"]] 
# result = pandas_series.ndim ## kaç boyutlu oldugunu söler
# result = pandas_series.dtype ## tipini söler
# result = pandas_series.shape ## (kaç elemanlı \ kaç boyutlu)
# result = pandas_series.sum() ## elemanları toplar
# result = pandas_series.max() ## maximum degeri söler
# result = pandas_series + pandas_series ## aynı indexdeki elemanları toplar
# result = pandas_series + 50 ## her elemana 50 ekler
# result = np.sqrt(pandas_series) ## elemanların kareköklerini alır
# result = pandas_series >= 50 ## 50 den büyük olanlar true
# result = pandas_series %2 == 0 ## çift olan elemanlar true

# print(pandas_series[result]) ## çift olan elemanları yazdırır
# print(pandas_series[pandas_series %2 == 0 ]) ## çift olan elemanları yazdırır
# print(pandas_series)
# print(result)


opel_2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel_2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel_2018 + opel_2019
# print(total)
print(total["astra"])