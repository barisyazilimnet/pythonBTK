# for x in range(50,100,10): # 50 den 100 e kadar sayıları 10 ar yazar
#     print(x)

# print(list(range(5,100,10)))

#enumarate
# index = 0
# greeting ="Hello There"
# for letter in greeting:
#     print(f"{index}.Kelime :{letter}")
#     index += 1

# greeting ="Hello There"
# for index, letter in enumerate(greeting):
#     print(f"{index}.Kelime :{letter}")

# zip
list1 =[1,2,3,4,5]
list2 =["a","b","c","d","e"]
list3 =[100,200,300,400,500]
# print(list(zip(list1,list2,list3)))

# for item in (zip(list1,list2,list3)):
#     print(item)
for a,b,c in (zip(list1,list2,list3)):
    print(a,b,c)