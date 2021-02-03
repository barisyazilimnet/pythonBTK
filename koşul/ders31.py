# 1 Girilen bir sayının 0 - 10 arasında olup olmadıgğını kontrol ediniz.

# sayi = float(input("Sayı :"))
# if (sayi >= 0) and (sayi <= 100):
#     print(f"Girdiğiniz sayı :{sayi} 0 ile 100 arasındadır")
# else:
#     print(f"Girdiğiniz sayı :{sayi} 0 ile 100 değildir")

# 2 Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

# sayi = float(input("Sayı :"))
# if (sayi > 0):
#     if (sayi % 2 == 0):
#         print("Girilen sayı pozitif çift sayıdır")
#     else:
#         print("Girilen sayı pozitif tek sayıdır")
# else:
#     print("Girilen sayı negatifdir")     

# 3 Email ve parola bilgileri ile giriş kontrolu yapınız
# email = "kurt-bar07@hotmail.com"
# password = "159753"

# girilen_email = input("Email :")
# girilen_password = input("Şifre :")

# if email == girilen_email:
#     if password == girilen_password:
#         print("Giriş başarılı")
#     else:
#         print("Şifre hatalı")
# else:
#     print("Email hatalı")

# 4 Girilen 3 sayıyı büyüklük olarak karşılaştırınız
# x = int(input("x :"))    
# y = int(input("y :"))    
# z = int(input("z :")) 

# if (x > y) and (x > z):
#     print("X en büyük sayıdır")
# elif (y > x) and (y > z):
#     print("Y en büyük sayıdır")
# else:
#     print("C en büyük sayıdır")

# 5 Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesapalyınız
# Eger ortalama 50 be üstündeyse geçti değilse kaldı yazdırın
# a-) ortalama 50 olsa bile final notu en 50 olmalıdır
# b-) finalden 70 alındığında ortalamanın önemi olmasın

# vize1 = float(input("vize1 :"))
# vize2 = float(input("vize2 :"))
# final = float(input("final :"))
# ortalama = (((vize1 + vize2)/2)*0.6) + (final * 0.4)
# print(f"Ögrencinin ortalaması :{ortalama}")

# a-)
# if (ortalama >=50):
#     if (final >= 50):
#          print("Geçme durumunuz başarılı")
#     else:
#         print("Geçme durumunuz başarısız. Finalden en az 50 almalısınız")
# else:
#     print("Geçme durumunuz başarısız")

# b-)
# if ortalama >= 50:
#     print("Geçme durumunuz başarılı")
# else:
#     if final >=70:
#         print("Geçme durumu başarılı. Finalden en az 70 aldığınız için geçtiniz")
#     else:
#         print("Geçme durumu başarısız")

# 6 Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
# Formül : Kilo /(boy**2)
# Aşagıdaki tabloya göre kişi hangi gruba girmektedir
# 0 - 18.4    => Zayıf
# 18.5 - 24.9 => Normal
# 25.0 - 29.9 => Fazla kilolu
# 30.0 - 34.9 => Şişman(obez)

name = input("Adınız :")
kg = float(input("Kilonuz :"))
hg = float(input("Boyunuz :"))
index = kg / (hg ** 2)
print(f"Vücut Kitle endeksiniz :{index}")

if (index >= 0) and (index <= 18.4):
    print("Zayıf")
elif (index >= 18.5) and (index <= 24.9):
    print("Normal")
elif (index >= 25.0) and (index <= 29.9):
    print("Fazla kilolu")
elif (index >= 30.0) and (index <= 34.9):
    print("Obez")
else:
    print("Hatalı bilgi girilmiştir")

