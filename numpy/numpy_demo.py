import numpy as np

# 1 - (10,15,30,45,60) degerlerine sahip numpy dizisi oluşturunuz
result = np.array([10,15,30,45,60])

# 2 - (5-15) arasındaki sayılarla numpy dizisi oluşturunuz
result = np.arange(5,15)

# 3 - (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz
result = np.arange(50,100,5)

# 4 - 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz
result = np.zeros(10)

# 5 - 10 elemanlı birlerden oluşan bir dizi oluşturunuz
result = np.ones(10)

# 6 - (0-100) arasında eşit aralıklı 5 sayı üretin
result = np.linspace(0,100,5)

# 7 - (10-30) arasında rastgele 5 tane tamsayı üretin
result = np.random.randint(10,30,5)

# 8 - [-1 ile 1] arasında 10 adet sayı üretin
result = np.random.randn(10)

# 9 - (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz
matrix = np.random.randint(10,50,15).reshape(3,5)

# 10 - Üretilen matrixin satır ve sütun sayıları toplamlarını hesaplayınız
# result = result.sum(axis = 1)
# result = result.sum(axis = 0)

# 11 - Üretilen matrixin en büyük ve en küçük ve ortalaması nedir 
# result = result.max()
# result = result.min()
# result = result.mean()

# 12 - Üretilen matrixin en büyük degerinin indexi kaçtır
result = result.argmax()

# 13 - (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz
numbers = np.arange(10,20)
result = numbers[:3]

# 14 - Üretilen dizinin elemanlarını tersten yazıdırın
result = numbers[::-1]

# 15 - Üretilen matrixin ilk satırını seçiniz 
result = matrix[0]

# 16 - Üretilen matrixin 2.satır ve 3. sütunundaki elemanı hangisidir
result = matrix[1,2]

# 17 - Üretilen matrixin tüm satırlardaki ilk elemanı seçiniz
result = matrix[:,0]

# 18 - Üretilen matrixin her bir elemanın karesini alınız
result = np.square(matrix)
result = matrix ** 2

# 19 - Üretilen matrixin elemanlarının hangisi pozitif çift sayıdır
#      Aralığı (-50,50) arasında yapınız
matrix = np.random.randint(-50,50,15)
positive = matrix[matrix > 0]
result = positive[positive %2 == 0]

print(result)