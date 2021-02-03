# 1- 100 e kadar
# x = 0
# while x <= 100:
#     if x %2 == 0:
#         print(f"Sayı çift :{x}")
#     else:
#         print(f"Sayı tek :{x}")
#     x += 1
# print("bitti...")

name ="" #False
while not name.strip():
    name = input("İsminizi giriniz :")
print(f"Merhaba, {name}")