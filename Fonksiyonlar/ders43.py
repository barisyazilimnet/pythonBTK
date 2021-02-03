# def change_name(n):
#     n = "Barış"

# name ="Yiğit"
# change_name(name)
# print(name)

# def change(n):
#     n[0] = "İstanbul"

# cities =["Ankara","İzmir"]
# n = cities[:]
# n[0] ="İstanbul"

# print(cities)
# print(n)

# # change(cities)
# # print(cities)

# def add(*params):
#     print(params)
#     return sum((params))

# print(add(10,20,30,50))
# print(add(10,30,50,60,70,80,90,100,20,30,))

# def display_user(**params):
#     for key,value in params.items():
#         print(f"{key} is {value}")

# display_user(name = "Çınar", age = 2, city = "İstanbul")
# display_user(name = "Ada", age = 12, city = "Kocaeli", phone = 121351)
# display_user(name = "Yiğit", age = 14, city = "Ankara", phone = 316321, email = "yigit@gamil.com")

def my_func(a,b,c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

my_func(10,20,30,40,50,60,70, key1 = "value1", key2 = "value2")
