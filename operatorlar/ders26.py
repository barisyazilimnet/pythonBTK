# 1 Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
# x = int(input("Sayi :"))
# result = 0 <= x <= 100

# 2 Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
# # result = (x > 0) and (x%2==0)

# # 3 Email ve parola bilgileri ile giriş kontrolü yapınız
# mail ="kurt-bar07@hotmail.com"
# password ="159753"
# input_email =input("Email giriniz :")
# input_password =input("Parola giriniz :")
# result = (mail == input_email) and (password == input_password)

# 4 Girilen 3 sayının  üyüklük olarak karşılaştırınız
# a = int(input("a :"))
# b = int(input("b :"))
# c = int(input("c :"))
# result = (a > b) and (a > c)
# print(f"a en büyük :{result}")

# result = (b > a) and (b > c)
# print(f"b en büyük :{result}")

# result = (c > b) and (c > a)
# print(f"c en büyük :{result}")

# # 5 Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız 
# # Eger kullanıcı 50 ve üstündeyse geçti değilse kaldı yazdırın 
# vize1 = float(input("vize1 :"))
# vize2 = float(input("vize2 :"))
# final = float(input("final :"))
# ortalama = (((vize1 + vize2)/2)*0.6) + (final * 0.4)
# # result = ortalama >=50 

# # a Ortalama 50 olsa bile final notu en az 50 olmalıdır
# # result = (ortalama >= 50) and (final >= 50)

# # b finalden 70 aldığında ortamalanın önemi olmasın
# result = (ortalama >= 50) or (final >= 70)
# print(f"geçti :{result}")

# 6 Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
    # Formül :(Kilo / boy uzunluğunun karesi)
    # Aşagıdaki tabloya göre kişi hangi gruba girmektedir
    # 0 - 18.4      => Zayıf
    # 18.5 - 24.9   => Normal
    # 25.0 - 29.9   => Fazla kilolu
    # 30.0 - 34.9   => şişman (obez)

name = input("Adınız :")
kg = float(input("Kilonuz :"))
boy = float(input("Boyunuz :"))

index = kg / (boy**2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
kilolu = (index >= 25.0) and (index <= 29.9)
obez = (index >= 30.0) and (index <= 34.9)

print(f"{name} kilo indeksin :{index} ve kilo değerlendirmen zayıf :{zayif}")
print(f"{name} kilo indeksin :{index} ve kilo değerlendirmen normal :{normal}")
print(f"{name} kilo indeksin :{index} ve kilo değerlendirmen kilolu :{kilolu}")
print(f"{name} kilo indeksin :{index} ve kilo değerlendirmen obez :{obez}")