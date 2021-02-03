# # class
# class person:
    
#     #class attributes
#     address ="no information"    
    
#     # constructor (yapıcı method)
#     def __init__(self, name, year):
    
#         #object attributes
#         self.name = name
#         self.year = year
    
#     #instance methods
#     def intro(self):
#         print("Hello There. I am " + self.name)
#     def calculate_age(self):
#         return 2019 - self.year

# #object (instance)
# p1 = person("Barış", 2000)
# p2 = person("Semih", 1999)

# # p1.intro()
# # p2.intro()

# print(f"Adım :{p1.name} Yaşın :{p1.calculate_age()}")
# print(f"Adım :{p2.name} Yaşın :{p2.calculate_age()}")

# # # updating
# # p1.name ="Ali"
# # p1.address ="Alanya"

# # # accessing object  attributes
# # print(f"p1 = name :{p1.name} year :{p1.year} address :{p1.address}")
# # print(f"p2 = name :{p2.name} year :{p2.year} address :{p2.address}")

# # print(p1)
# # print(p2)
# # print(type(p1))
# # print(type(p2))

class circle:
    #class object attributes
    pi = 3.14

    def __init__(self, yari_cap = 1):
        self.yari_cap = yari_cap
    
    # methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yari_cap
        
    def alan_hesapla(self):
        return self.pi * (self.yari_cap ** 2)
    
c1 = circle() # yarı çap belirtilmedigi için 1 olarak alcak
c2 = circle(5)

print(f"c1 = alan :{c1.alan_hesapla()} çevre :{c1.cevre_hesapla()}")
print(f"c2 = alan :{c2.alan_hesapla()} çevre :{c2.cevre_hesapla()}")