name = "Barış KURT"
# for letter in name:
#     if letter == "ı":
#         continue
#     print(letter)

# for letter in name:
#     if letter == "T":
#         break
#     print(letter)

# x = 0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1
# x = 0
# while x < 5:
#     x += 1
#     if x == 2:
#         continue
#     print(x)

x = 0
toplam =0
while x <= 100:
    x +=1
    if x %2 ==1:
        continue
    toplam += x
print(f"Toplam :{toplam}")