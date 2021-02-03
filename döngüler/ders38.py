# numbers =[x for x in range(10)]
# print(numbers)

# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers)

# for x in range(10):
#     print(x**2)

# numbers =[x**2 for x in range(10)]
# print(numbers)

# numbers =[x**2 for x in range(10) if x%3==0]
# print(numbers)

# my_string ="Hello"
# my_list =[]

# for letter in my_string:
#     my_list.append(letter)
# print(my_list)

# my_list =[letter for letter in my_string]
# print(my_list)

# years =[1983, 1999, 2008, 1956, 1986]
# ages =[2019-year for year in years]
# print(ages)

# numbers =[x if x%2 == 0 else "TEK" for x in range(1,10)]
# print(numbers)

result =[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers =[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)