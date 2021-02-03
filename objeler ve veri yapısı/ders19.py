fruits ={"orange","apple","banana"}

# print(fruits[0]) kullanılamaz
# sıralanamaz

for x in fruits:
    print(x)

fruits.add("cherry") #eleman ekler
fruits.update(["mango","grape"]) # var olan eleman eklenmeye çalışılırsa sadece  sefer eklenir 2. sefer eklenemez
# silme işlemi yapar
fruits.remove("mango")
fruits.discard("apple")
# fruits.pop() herhangi bir elemnaı siler
fruits.clear() #bütün elemanları siler

my_list =[1,2,4,5,4,2,1]
print(my_list)
print(set(my_list)) # tekrarlanan değerleri siler