name = "barış"
surname = "KURT"
age = 20

greeting = "My name is "+name+" "+surname+"\nI am "+str(age)+" years old"
length = len(greeting)

# print(greeting) My name is barış KURT
#                 I am 20 years old
# print(greeting[0])  M   0. karakteri yazdır
# print(greeting[3])  n  3. karakteri yazdır
# print(len(greeting)) 39  uzunluk
# print(greeting[length-1]) d  sondan 1 ilk karakteri yazdır
# print(greeting[-1]) d     sondan 1 ilk karakteri yazdır
# print(greeting[3:7]) name  3 ile 7 arasındaki karakterleri yazdır
# print(greeting[3:]) name is barış KURT  3ten sonraki karakterleri yazdır
                    # I am 20 years old
# print(greeting[:16])    My name is barış     0 dan 16 ya kadar olan karakterleri yazdır
print(greeting[2:40:2])     # aei aı UTIa 0yasod     2 den 40. karaktere olan karakterleri 2 şer yazdır