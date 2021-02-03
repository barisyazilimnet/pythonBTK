# bellek üzerinde yer kaplamaz
# burdaki bilgilere sadece bir defa ulaşabilir
# def cube():
#     for i in range(5):
#         yield i**3

# for i in cube():
#     print(i)


# burdakilere gerek yoktur üstteki gibi kullanılabilir
# iterator = cube() #zaten iterator object

# for i in iterator:
#     print(i)

# generator = cube()
# iterator = iter(generator)  # bu ikisine gerek yok

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))