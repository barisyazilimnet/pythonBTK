import requests

class Github:
    def ___init___(self):
        self.api_url = "https://api.github.com/users/"

    def getUser(self, username):
        response = requests.get(self.api_url + username)
        return response.json()

github = Github()

while True:
    choose = input("1 - Kullanıcı ara\n2 - Çalışmaları görüntüle\n3 - Çalışma oluştur\n4 - Çıkış\nSeçiminiz : ")

    if choose == "4":
        break
    else:
        if choose == "1":
            username = input("Kullanıcı adı :")
            result = github.getUser(username)
            # print(f"İsim :{result['name']} depolar :{result['public_repo']} takipçiler :{result['followers']}")
        elif choose == "2":
            pass

        elif choose == "3":
            pass

        else:
            print("Yanlış seçim")


# Btk 15.9 github api dersi 
# Hata veriyor