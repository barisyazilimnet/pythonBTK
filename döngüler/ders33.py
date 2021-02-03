numbers =[1,3,5,7,9,12,19,21]

# 1 numbers listesindeki hangi sayılar 3 ün katıdır
# for number in numbers:
#     if number %3 == 0:
#         print(number)

# 2 numbers listesinde sayıların toplamı kaçtır
# toplam = 0
# for number in numbers:
#     toplam += number
# print(f"Toplam :{toplam}")

# 3 numbers listesindeki tek sayıların karesini alınız
# kare = 0
# for number in numbers:
#     if number %2 == 1:
#         kare = number ** 2
#         print(f"Sayi :{number} Karesi :{kare}")

sehirler =["Kocaeli", "İstanbul", "Ankara", "İzmir", "Rize"]

# 4 Şehirlerden hangileri en fazla 5 karakterlidir
# for sehir in sehirler:
#     if len(sehir) <= 5:
#         print(sehir)

products =[
    {"name" :"samsung s6", "price" :3000},
    {"name" :"samsung s7", "price" :4000},
    {"name" :"samsung s8", "price" :5000},
    {"name" :"samsung s9", "price" :6000},
    {"name" :"samsung s10", "price" :7000}
]
# 5 Ürünlerin toplam fiyatı nedir
# toplam = 0
# for product in products:
#     toplam += product["price"]
# print(f"Toplam :{toplam}")

# 6 Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz
for product in products:
    if product["price"] <= 5000:
        print(product["name"])