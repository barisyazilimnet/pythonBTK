# numbers =[1,3,5,7,9,12,19,21]

# 1 numbers listesini wihle ile ekrana yazdırın
# x = 0
# while x < len(numbers):
#     print(numbers[x])
#     x += 1
# 2 Başlanıç ve bitiş değerlerinş kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
# start = int(input("Başlangıç :"))
# stop = int(input("Bitiş :"))

# i = start
# while i < stop:
#     i +=1
#     if i %2 == 1:
#         print(i)

# 3 1 - 100 arasındaki sayıları azalan şekilde yazdırın
# x = 100
# while x >= 1:
#     print(x)
#     x -= 1

# 4 Kullanıcıdan alacagınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
# numbers = []
# x = 0
# while x < 5:
#     number = int(input("Sayı :"))
#     numbers.append(number)
#     x += 1
# print(numbers)

# 5 Kullanıcıdan alacagınız sınırsız ürün bilgisini ürünler listesine ekleyiniz
# ** Üürün sayısını Kullanıcıya sorun
# ** Dictionary listesi yapısı (name,price) şeklinde olsun
# ** Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile yazdırın

products =[]
piece = int(input("Kaç adet ürün eklemek istiyorsunuz :"))
x = 0
while x < piece:
    name = input("Ürün ismi :")
    price = input("Ürün fiyatı :")
    products.append({
        "name" :name, "price" :price
    })
    x += 1
for product in products:
    print(f"Ürün adı :{product['name']} Ürün fiyatı :{product['price']}")