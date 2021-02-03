names,years =["Ali","Yağmur","Hakan","Deniz"], [1998,2000,1998,1987]

# 1 "Cenk" ismini listenin sonuna ekleyin
# names.append("Cenk")

# 2 "Sena" değerini listenin başına ekleyiniz
# names.insert(0,"Sena")


# 3 "Deniz" ismini listeden siliniz
# names.remove("Deniz")

# 4 "Deniz" isminin index numarasını bulunuz
# result = names.index("Deniz")

# 5 "Ali" listenin bir elemanıdır
# result = "Ali" in names

# 6 Liste elemanlarını ters çevirin
# result =names[::-1]
# result =years[::-1]
# names.reverse()
# years.reverse()

# 7 liste elemanlarını alfabetik olarak sıralayınız
# names.sort()
# result = names

# 8 years listesini rakamasal büyüklüğe göre sıralyınız
# years.sort()
# result =years

# 9 str ="Chevrolet,Dacia" karakter dizisini listeye çeviriniz
# str ="Chevrolet,Dacia"
# result =str.split(",")

# 10 years listesinin en büyük ve en küçük elemanı nedir
# result =max(years)
# result =min(years)

# 11 years listesinde kaç tane "1998" değeri vardır
result =years.count(1998)

# 12 years listesinin tüm elemanlarını siliniz
years.clear()
result = years

# 13 kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar =[]
marka = input("marka :")
markalar.append(marka)
marka = input("marka :")
markalar.append(marka)
marka = input("marka :")
markalar.append(marka)
print(markalar)