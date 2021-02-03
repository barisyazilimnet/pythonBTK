file = open("newfile.txt", encoding="utf-8")

# for döngüsü
# for i in file:
#     print(i, end="")

# read() fonksiyonu
# content =file.read()
# print(content)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)

# print(content)

# readline() fonksiyonu
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")

# readlines() fonksiyonu

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])




file.close()