import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2 # aynı indexdeki sayıları toplar
result = numbers1 + 10 # bütün indexdeki degerlere 10 ekler
result = numbers1 - numbers2 # aynı indexdeki sayıları çıkarır
result = numbers1 - 10 # bütün indexdeki degerlerden 10 çıkarır
result = numbers1 * numbers2 # aynı indexdeki sayıları çarpar
result = numbers1 * 10 # bütün indexdeki degerleri 10 ile çarpar
result = numbers1 / numbers2 # aynı indexdeki sayıları böler
result = numbers1 / 10 # bütün indexdeki degerleri 10 ile böler
result = np.sin(numbers1) # dizideki bütün degerlerin sinüsünü alır
result = np.cos(numbers1) # dizideki bütün degerlerin kosünüsünü alır
result = np.sqrt(numbers1) # dizideki bütün degerlerin kareköklerini alır
result = np.log(numbers1) # dizideki bütün degerlerin logaritmasını alır alır

multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)
# print(multi_numbers1)
# print(multi_numbers2)

result = np.vstack((multi_numbers1,multi_numbers2)) # 2. matrixi 1. matrixin devamına ekleyerek birleşti
result = np.hstack((multi_numbers1,multi_numbers2)) # aynı satırdaki indexleri birleştirir
result = numbers1 >= 50 # dizideki bütün elemanlar 50 den büyükse true deger verir ve küçük olanlarada false deger verir
result = numbers1 % 2 == 0 # dizideki bütün elemanların bölümden kalan 0 ise true deger yanlış ise false deger verir
print(numbers1[result])
print(result)
