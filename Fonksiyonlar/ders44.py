# 1 Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız

# def yazdir(word, piece):
#     print(word * piece)

# yazdir("Merhaba\n",)

# 2 Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız

# def listeye_cevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeye_cevir(10,20,30,"Merhaba")
# print(result)

# 3 Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
# def asal_sayilari_bul(x, y):
#     for sayi in range(x , y+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 print(sayi)
# x = int(input("Sayi 1 :"))
# y = int(input("Sayi 2 :"))
# asal_sayilari_bul(x, y)

# 4 Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz

def tam_bolenleri_bul(sayi):
    tam_bolenler = []

    for i in range(2,sayi):
        if sayi % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler

print(tam_bolenleri_bul(20))