# Inheritance (Kalıtım): Miras alma

# person => name, lastname, age, eat(), run(), drink()
# student(person), teacher(person)

# animal => dog(), cat()

class person():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        print("person created")
    
    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am a eating")

class student(person):
    def __init__(self, fname, lname, number):
        person.__init__(self, fname, lname)
        self.student_number = number
        print("student created")

    # override
    def who_am_i(self):
        print("I am a student")

    def say_hello(self):
        print("Hello. I am a student")

class teacher(person):
    def __init__(self, fname, lname, brunch):
        super().__init__(fname, lname) # person class yazmak yerine yazılır
        self.brunch = brunch

    def who_am_i(self):
        print(f"I am a {self.brunch} teacher")

p1 = person("Barış", "Kurt")
s1 = student("Semih", "Acar", 1562)
t1 = teacher("Mehmet", "Kurt", "Math")

print(p1.first_name +" "+ p1.last_name)
print(s1.first_name +" "+ s1.last_name +" "+ str(s1.student_number))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
s1.say_hello()