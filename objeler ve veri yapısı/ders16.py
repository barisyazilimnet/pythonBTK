list =[1,2,3]
tuple =(1,"iki",3)
# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list =["Ali","Veli"]
tuple =("Damla","Ayşe","Ayşe")

list[0] ="Barış"
# tuple[0] ="Fatma"  burası hata verecektir çünkü tuple listelerin içerigi degiştirelemez

print(tuple.count("Ayşe"))  #tuple tarzı listeler için sadece bu iki method kullanılabilir
print(tuple.index("Ayşe"))

names =("Demet","Fatma","Ayşe") + tuple
print(list)
print(tuple)
print(names)