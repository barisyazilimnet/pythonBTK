message = "Hello. My name is Barış KURT"
# message = message.upper()  bütün karakterleri büyük yazdır
# message = message.lower()   bütün karakterleri küçük yazdır
# message = message.title()     her kelimenin ilk harfini büyük yap
# message = message.capitalize()  sadece ilk kelimeyi büyük yap sonraki kelimeleri küçük
# message = message.strip()     baştaki boşluk karakterini sil
# message = message.split()     boşluk karakterlerinden ayırıp diziye koy
# message = message.split(".")  noktadan ayırma    
# message = " ".join(message)   tekrar birleştir ve birleştirirken araya boşluk koy
# find = message.find("Barış")  degişkende Barış kelimesini bul
# print(find)
# isfound = message.startswith("H") degişken H ile mi başlıyor
# isfound = message.endswith("T")   degişken T ile mi bitiyor
# print(isfound)
# message = message.replace("My name is","Benim adım")  My name is kelimesini Benim adım la degiştir
# message = message.replace(" ","*").replace("H","h")
# message = message.center(50,"*") Cümleyi 50 karaktere tamala ve boş kalan yerlere * koy
print(message)