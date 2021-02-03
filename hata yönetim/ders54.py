# error handling => hata yönetimi

# try:
#     x = int(input("x :"))
#     y = int(input("y :"))
#     print(x/y)

# except ZeroDivisionError: # 0 bölme hatası
#     print("y için sıfır girilemez")
# except ValueError: # hatalı deger girilmesi
#     print("x ve y için sayısal deger giriniz")

# except (ZeroDivisionError, ValueError) as e: #iki hatada da aynı yazıyı gösterir
#     print("yanlış bilgi girdiniz")
#     print(e) # ahngi objeden gelen hata oldugunu gösterir

# try:
#     x = int(input("x :"))
#     y = int(input("y :"))
#     print(x/y)

# except:
#     print("yanlış bilgi girdiniz") # standart hata mesajıdır

# try:
#     x = int(input("x :"))
#     y = int(input("y :"))
#     print(x/y)

# except:
#     print("yanlış bilgi girdiniz") # standart hata mesajıdır
# else:
#     print("herşey yolunda")

while True:
    try:
        x = int(input("x :"))
        y = int(input("y :"))
        print(x/y)

    except:
        print("yanlış bilgi girdiniz") # standart hata mesajıdır
    else:
        break
    