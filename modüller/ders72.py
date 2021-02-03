import json, os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class user_repository:
    def __init__(self):
        self.users =[]
        self.is_logged_in = False
        self.current_user = {}

        self.load_users()

    def load_users(self):
        if os.path.exists("users.json"):
            with open("users.json", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    new_user = User(username = user["username"], password = user["password"], email = user["email"])
                    self.users.append(new_user)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.save_to_file()
        print("Kullanıcı oluşturuldu")
    
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.is_logged_in = True
                self.current_user = user
                print("Giriş yapıldı")
                break
        
    def logout(self):
        self.is_logged_in = False
        self.current_user ={}
        print("Çıkış yapıldı")

    def identity(self):
        if self.is_logged_in:
            print(f"username :{self.current_user.username}")
        else:
            print("Giriş yapılmadı")

    def save_to_file(self):
        list =[]

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(list, file)

repository = user_repository()

while True:
    print("Menü".center(50,"*"))
    choose = input("1 - Kayıt ol\n2 - Giriş yap\n3 - Oturumu kapat\n4 - Kimlik bilgisi\n5 - Çıkış\nSeçiminiz: ")
    
    if choose == "5":
        break
    else:
        if choose == "1":
            username = input("Kullanıcı adı:")
            password = input("Parola:")
            email = input("Email:")

            user = User(username = username, password = password, email = email)
            repository.register(user)

        elif choose == "2":
            if repository.is_logged_in:
                print("Zaten giriş yapıldı")
            else:
                username = input("Kullanıcı adı:")
                password = input("Parola:")
                repository.login(username, password)

        elif choose == "3":
            repository.logout()
        
        elif choose == "4":
            repository.identity()
        
        else:
            print("Yanlış seçim")