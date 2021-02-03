import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10) # 1 ile 10 arasında bir dizi oluşturur
# result = np.arange(10,100,3) # 10 ile 100 arasında bir dizi oluşturur artış miktarı 3 dür
# result = np.zeros(10) # 10 tane 0 dan oluşan dizi yapar
# result = np.ones(10) # 10 tane 1  den oluşan dizi yapar
# result = np.linspace(0,100,5) # 0 ile 100 arasında 5 tane elemandan oluşan sabit artışı olan dizi oluşturur
# result = np.linspace(0,5,5)
# result = np.random.randint(0,10) #0 ile 10 arasında sayı oluşturur
# result = np.random.randint(20) #0 ile 20 arasında sayı oluşturur
# result = np.random.randint(1,10,3) # 1 ile 10 arasında 3 tane sayı oluşturur
# result = np.random.rand(5) #0 ile 1 arasında 5 tane sayı oluşturur
# result = np.random.randn(5) #0 ile 1 arasında negatif degerlerde dahil olmak üzere 5 tane sayı oluşturur
# np_array = np.arange(50) # 0 dan 50 ye kadar sayı oluşturur
# np_multi = np_array.reshape(5,10) # seçilen diziyi 5 satır 10 sütundan oluşan matrix e dönüştürür
# print(np_multi.sum(axis = 1)) # satırların toplamını verir
# print(np_multi.sum(axis = 0)) # sütunların toplamını verir
rnd_numbers = np.random.randint(1,100,10) #1 ile 100 arasında 10 tane sayı oluşturur
print(rnd_numbers)
# result = rnd_numbers.max() # üretilen dizide max degeri verir
# result = rnd_numbers.min() # üretilen dizide min degeri verir
# result = rnd_numbers.mean() # üretilen dizideki sayıların ortalamasını verir
# result = rnd_numbers.argmax() # üretile dizide max degerin kaçıncı index de oldugunu söler
result = rnd_numbers.argmin() #üretilen dizide min degerin kaçıncı index de oldugunu söler
print(result)