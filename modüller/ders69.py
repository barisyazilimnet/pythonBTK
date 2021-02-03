import os, datetime

# result = os.name # nt => windows
# os.chdir("C:\\") # C dizinine gider
# os.chdir("..") # bir alt klasore gider
# os.chdir("..") # bir daha bir alt klasore gider
# os.chdir("../..") # üstekiler yerine kullanırlır her iki noktada bir alt klasore gider
# result = os.getcwd() #hangi klasorde oldugunu söler
# os.mkdir("new directory") # bulunan yerde klasor oluşturur
# os.makedirs("new directory/yeni klasor") # iç içe klasor oluşturur
# os.makedirs("C:\\new directory2/yeni klasor")
# result = os.listdir() # bulundugu klasordeki dosyaları veya klasorleri gösterir
# result = os.listdir("C:\\") # C deki klasorleri listeler

# for file in os.listdir():         
#     if file.endswith("r"):  sonu r ile biten dosyaları veya klasorleri listeler
#         print(file)

# result = os.stat("1.docx") # dosya hakkında bilgiler verir
# result = result.st_size/1024 # dosya boyutunu kilobayt türünden verir
# result = datetime.datetime.fromtimestamp(result.st_ctime) # dosyanın oluşturulma tarihini verir
# result = datetime.datetime.fromtimestamp(result.st_atime) # dosyaya son erişilme tarihini verir
# result = datetime.datetime.fromtimestamp(result.st_mtime) # dosyanın degiştirilme tarihini verir

# os.system("chrome.exe")

# os.rename("new directory","yeni klasör") klasor adı degiştirir
# os.rmdir("new directory") klasor siler
# os.removedirs("yeni klasör/yeni klasor") iç içe klasorleri siler

#path modulü
result = os.path.abspath("ders52.py") # dosya yolunu söler
result = os.path.dirname("C:/Users/kurt-/Google Drive/BTK/python/ders52.py") # dizini gösteririr
result = os.path.dirname(os.path.abspath("ders52.py")) # dizini gösterir
result = os.path.exists("C:/Users/kurt-/Google Drive/BTK/python/modüller/ders52.py") # dosya ve klasor varlıgını sorgulama
result = os.path.isdir("C:/Users/kurt-/Google Drive/BTK/python/modüller") # dizin mu diye sorgular
result = os.path.isfile("C:/Users/kurt-/Google Drive/BTK/python/modüller/ders52.py") # dosya mı diye sorgular
result = os .path.splitext("ders52.py") # dosyanın uzantısıyla ismini ayırır

print(result)