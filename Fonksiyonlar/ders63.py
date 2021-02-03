# def us_alma(number):
#         def inner(power):
#         return number ** power
#     return inner

# two = us_alma(2)
# three = us_alma(3)
# print(two(3))
# print(three(3))

# def yetki_sorgula(page):
#     def inner(role):
#         if role == "admin":
#             return f"{role} rolü {page} sayfasına ulaşabilir"
#         else:
#             return f"{role} rolü {page} sayfasına ulaşamaz"
#     return inner

# user = yetki_sorgula("Product edit")
# print(user("admin"))
# print(user("user"))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi =="toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,2,3,5,9,7,50,60,70))

carpma = islem("çarpma")
print(carpma(50,6))

