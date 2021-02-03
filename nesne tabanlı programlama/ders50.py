my_list = [1,2,3]
# my_string = "my string"

# print(len(my_list))
# print(len(my_string))
# print(type(my_list))
# print(type(my_string))

class movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")
    
    def __str__(self):
        return f"adı :{self.title} yönetmen adı :{self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie silindi")

m = movie("film", "yönetmen", 120)

# print(str(my_list))
# print(str(m))
# print(len(my_list))
# print(len(m))
del m
# print(type(m))
# print(len(m))