liste =[1,2,3,4,5]

iterator = iter(liste)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in liste:
#     print(i)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break