# 1 Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise yada üniversite olmalıdır.

# name = input("Adınız :")
# age = int(input("Yaşınız :"))
# education = input("Eğitim durumunuz :".lower())

# if age >= 18:
#     if education == "lise" or education == "üniversite":
#         print("Ehliyet alabilirsiniz")
#     else:
#         print("Eğitim durumunuz uygun değildir")
# else:
#     print("Yaşınız uygun değildir")

# 2 Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaylayan ve ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız
    # 0 - 24 => 0
    # 25 - 44 => 1
    # 45 - 54 => 2
    # 55 - 69 => 3
    # 70 - 84 => 4
    # 85 - 100 => 5

# yazili1 = float(input("1. Yazılı notunuz :"))
# yazili2 = float(input("2. Yazılı notunuz :"))
# sozlu = float(input("Sözlü notunuz :"))

# ortalama = (yazili1 + yazili2 + sozlu )/3

# if (ortalama >= 0) and (ortalama <= 24):
#     print("Notunuz 0")
# elif (ortalama >= 25) and (ortalama <= 44):
#     print("Notunz 1")
# elif (ortalama >= 45) and (ortalama <= 54):
#     print("Notunuz 2")
# elif (ortalama >= 55) and (ortalama <= 69):
#     print("Notunuz 3")
# elif (ortalama >= 70) and (ortalama <= 84):
#     print("Notunuz 4")
# elif (ortalama >= 84) and (ortalama <= 100):
#     print("Notunuz 5")
# else:
#     print("Yanlış bilgi girdiniz")

# 3 Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşagıdaki bilgilere göre hesaplayınız
# 1. Bakım => 1.yıl
# 2. Bakım => 2.yıl
# 3. Bakım => 3.yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız

import datetime
tarih = input("Aracınız trafige çıkış tarihi nedir (3/5/2020) :")
tarih =tarih.split("/")
trafige_cikis = datetime.datetime(int(tarih[2]), int(tarih[1]), int(tarih[0]))
simdi = datetime.datetime.now()
fark = simdi - trafige_cikis
days = fark.days

if days <= 365:
    print("1. Servis aralığı")
elif (days > 365) and (days <= 365*2):
    print("2. Servis aralığı")
elif (days > 365*2) and (days <= 365*3):
    print("3. Servis aralığı")
else:
    print("Hatalı tarih girişi yapıldı")