course ="Semih ACAR ile Barış KURT çok iyi yerlere gelecekler"
website ="https://www.brs.com"

# 1 " Hello world " karakter dizisinin baştaki ve sondaki boşluk karakterlerini silin
result =" Hello world ".strip()

# 2 "www.brs.com" içindeki brs bilgisi haricindeki her karakteri silin
result = website.lstrip("htps:/")
result = result.strip("w.com")

# 3 course karakter dizisinin tüm karakterlerini küçük yapın
result = course.lower()

# 4 website içinde kaç tane s karakteri vardır
result = website.count("s")

# 5 website "www" ile başlayıp "com" ile mi bitiyor
result = website.startswith("www")
result = website.endswith("com")

# 6 website içinde ".com" ifadesi varmı
result = website.find(".com")
result = website.find(".com",0,10) #0 ile 10. karakterler arasında ara

# 7 course içindeki karakterlerin hepsi alfabetik mi
result = course.isalpha() # karakterler sözel mi boşluk karakterleri olduğu için hata veriyor
result = course.isdigit() # karakterler sayısal mı 

# 8 "Contents" ifadesindeki satırda 50 karakter içine yerleştirip sağ  ve soluna "*" yerleştirin
result ="Contents".center(50,"*")
result ="Contents".ljust(50,"*")
result ="Contents".rjust(50,"*")

# 9 course karakter dizisindeki tüm boşluk karakterlerini "-" degiştirin
result = course.replace(" ","-")
result = course.replace(" ","") #boşluk karakterlerini siler
result = course.replace(" ","-",5) #ilk 5 karakteri değiştir

# 10 "Hello World" karakter dizisinin "World" ifadesini "There" olarak degiştirin
result ="Hello World".replace("World","There")

# 11 course karakter dizisini boşluk karakterlerinden ayırın
result = course.split()
print(result)