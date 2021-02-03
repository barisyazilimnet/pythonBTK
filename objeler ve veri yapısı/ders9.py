course ="Semih ACAR ile Barış KURT çok iyi yerlere gelecekler"
website ="https://www.brs.com"

# 1 "course" karakter dizisinde kaç karakter bulunmaktadır
result = len(course)

# 2 "website" içinden www  karakterlerini alın
result = website[8:11]

# 3 "website" içinde com karakterlerini alın
result = website[16:]
result = website[-3:]

# 4 "course" içinden ilk 15 ve son 15 karakterlerini alın
result = course[:15]
result = course[-15:]

# 5 "course" ifadesindeki karakterleri tersden yazdırın
result = course[::-1]

name, surname, age, job = "Barış","KURT",20,"Yazılım Mühendisi"
# 6 Yukarıda verilen değişkenler ile aşağıdaki ifadeyi yazdırın
# "Benim adım Barış KURT, yaşım 20 ve mesleğim Yazılım Mühendisi"
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"

# 7 "Hello world" ifadesindeki w harfini "W" ile değiştirin
s ="Hello world"
result = s[:6] +"W"+s[-4:]

# 8 "abc" ifadesini 3 defa yanyana yazdırın
result = "abc "*3
print(result)