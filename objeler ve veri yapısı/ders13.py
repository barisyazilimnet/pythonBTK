# 1 "BMW, Mercedes, Opel, Mazda" elemanlarına sahip liste oluşturunuz
list = ["BMW", "Mercedes", "Opel", "Mazda"]

# 2 Liste kaç elemanlıdır
result = len(list)

# 3 listenin ilk elemanı ve son elemanı nedir
result = list[0]
result = list[-1]

# 4 Mazda elemanını Toyota ile değiştirin
list[-1] = "Toyota"
result = list

# 5 Mercedes listenin bir elemanımıdır
result = "Mercedes" in list

# 6 listenin -2 indeksindeki değer nedir
result = list[-2]

# 7 listenin ilk 3 elemanını alın
result = list[:3]

# 8 Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini koyun
list[-2:] = ["Toyota", "Renault"]
result = list

# 9 listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
result = list + ["Nissan", "Audi"]

# 10 listenin son elemanını silin
del list[-1] 
result = list

# 11 liste elemanlarını tersten yazdırın
result = list[::-1]

# 12 Aşagıdaki verileri liste içinde saklayın
# Student_A =["Yiğit","Bilgi",2010,[70,60,70]]
# Student_B =["Sena","Turan",1999,[80,80,70]]
# Student_C =["Ahmet","Turan",1998,[80,70,90]]
Student_A =["Yiğit","Bilgi",2010,[70,60,70]]
Student_B =["Sena","Turan",1999,[80,80,70]]
Student_C =["Ahmet","Turan",1998,[80,70,90]]
Students = Student_A + Student_B + Student_C

# 13 liste elemanlarını yazdırın
result = Students
print(result)