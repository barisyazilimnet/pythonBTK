# # key -> value
# # 41 => Kocaeli  34 => İstanbul

# sehirler =["Kocaeli","İstanbul"]
# plakalar =[41,34]

# # print(plakalar[sehirler.index("İstanbul")])

# # print(plakalar["Kocaeli"]) => 41
# # print(plakalar["İstanbul"]) => 34

# plakalar ={"Kocaeli" : 41, "İstanbul" : 34}
# # print(plakalar["Kocaeli"])
# # print(plakalar["İstanbul"])

# plakalar["Ankara"] = 6
# plakalar["Kocaeli"] ="New value"

# print(plakalar)

users ={
    "Barış KURT" :{
        "age" : 20,
        "roles" :["admin","user"],
        "e_mail" : "kurt-bar07@hotmail.com",
        "adress" : "Alanya",
        "phone" : "532 497 38 73"
    }, 
    "Semih ACAR" :{
        "age" : 26,
        "roles" :["admin","user"],
        "e_mail" : "semih_acar01@hotmail.com",
        "adress" : "Adana",
        "phone" : "535 683 41 85"
    }
}

print(users["Barış KURT"]["age"])
print(users["Barış KURT"]["e_mail"])
print(users["Barış KURT"]["adress"])
print(users["Barış KURT"])