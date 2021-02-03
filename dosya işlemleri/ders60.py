# with open("newfile.txt", "r+",encoding="utf-8") as file:
#     file.write("deneme123456789") # imlecin bulundugu (başlangıçta 0dır) yerden yazmaya başlar eger bir şey yazıyorsa siler 

# with open("newfile.txt", "r+",encoding="utf-8") as file:
#     print(file.read())

# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nBarış Kurt") sayfa sonuna eklme yapar

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Barış KURT\n" + content
#     file.seek(0)
#     file.write(content) sayfa başına ekleme yapar

with open("newfile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Semih acar")
    print(list)