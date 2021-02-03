# 1 Girilen 2 sayıdan hangisi büyüktür
# a = int(input("a :"))
# b = int(input("b :"))
# result = a > b
# print(f"a :{a} b :{b} den büyüktür :{result}")

# 2 Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortlama hesaplayınız
#   Eğer ortalama 50 ve üstündeyse geçti degilse kaldı yazdırın
# vize1 = float(input("1. vize :"))
# vize2 = float(input("2. vize :"))
# final = float(input("final :"))
# ortalama = (((vize1 + vize2)/2)*0.6) + (final*0.4)
# print(f"Not ortalamanız :{ortalama} ve dersten geçme durumunuz :{ortalama>=50}")

# 3 Girilen bir sayının tek mi çift mi olduğunu yazdırın
# x = int(input("Sayi girin :"))
# x %= 2
# print(f"Girdiginiz sayı çift :{x == 0}")

# 4 Girilen sayının negatif pozitif durumunu yazıdırn
# x = int(input("Sayı girin :"))
# x = x > 0
# print(f"Girdiginiz sayı pozitif olma durumu :{x}")

# 5 Parola ve email bilgisini isteyip doğrulugunu kontrol ediniz
email ="kurt-bar07@hotmail.com"
password ="159753"

x = input("e-mail giriniz :")
y = input("şifre giriniz :")

print(f"E-mail doğru olma durumu :{email == x} \nŞifre doğru olma durumu :{password == y}")