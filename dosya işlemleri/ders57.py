# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# kullanımı : open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir

# "w" (write) yazma modu dosya konumda oluşturulur
    # ** dosya içeriğini siler yeniden ekleme yapar

# file = open("newfile.txt","w")
# file.close()

# file = open("C:/users/kurt-/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt", "w", encoding="utf-8")
# file.write("Barış KURT")
# file.close()

# "a" (append) ekleme dosya konumda yoksa oluşturulur

# file = open("newfile.txt", "a", encoding="utf-8")
# file.write("Barış KURT\n")
# file.close()

# "x" (create) oluşturma dosya zaten varsa varsa hata verir

# file = open("newfile2.txt", "x", encoding="utf-8")

# "r" (read) okuma varsayılan dosya konumda yoksa hata verir

# file = open("newfile.txt", encoding="utf-8")

# print(file)