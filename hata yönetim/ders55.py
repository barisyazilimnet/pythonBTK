# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 8 karakter olmalıdır.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola rakam harf içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Parola alpha numeric karakter içermelidir.")
#     elif re.search("\s", psw):
#         print("Parola boşluk içermemelidir.")
#     else:
#         print("Parolanız başarıyla oluşturuldu")

# password ="123456aA_"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)

class person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor.")
        else:
            self.name = name