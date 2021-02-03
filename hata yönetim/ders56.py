liste =["1","2","5a","10b","abc","10","50"]

# 1 liste elemanları içindeki sayısal değerleri bulunuz
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2 Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazınız
# while True:
#     sayi = input("sayı :")
#     if sayi == "q":
#         break

#     try:
#         result = float(sayi)
#         print("Girdiğiniz sayı :",result)
#     except ValueError:
#         print("Geçersiz sayı")
#         continue

# 3 Girilen parola içinde türkçe karakter hatası veriniz
# turkce_karakterler ="şçğüıİ"

# password = input("Parola :")

# for i in password:
#     if i in turkce_karakterler:
#         raise TypeError("Parola türkçe karakter içeremez.")
#     else:
#         pass

# print("Geçerli parola")

# 4 Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları veriniz
def Faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer")

    result = 1

    for i in range(1, x + 1):
        result *= i

    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y = Faktoriyel(x)
    except ValueError as error:
        print(error)
        continue
    print(y)