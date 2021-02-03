# Bankamatik uygulamsı

Baris_hesap ={
    "ad" : "Barış KURT",
    "hesap_no" : "1235489",
    "bakiye" : 3000,
    "ek_hesap" : 2000
}

Ali_hesap ={
    "ad" : "Ali ",
    "hesap_no" : "1562596",
    "bakiye" : 2000,
    "ek_hesap" : 1000
}

def para_cek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiye_sorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ek_hesap"]

        if toplam >= miktar:
            ek_hesap_kullanimi = input("Ek hesap kullanılsın mı (e/h) :")

            if ek_hesap_kullanimi == "e":
                ek_hesap_kullanılacak_miktar = miktar - hesap["bakiye"]
                hesap["ek_hesap"] -= ek_hesap_kullanılacak_miktar
                print("Paranızı alabilirsiniz")
                bakiye_sorgula(hesap)
            else:
                print(f"{hesap['hesap_no']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print("ÜZgünüz. Bakiyeniz yetersiz")
            bakiye_sorgula(hesap)

def bakiye_sorgula(hesap):
    print(f"{hesap['hesap_no']} nolu hesabınızda {hesap['bakiye']} ₺ bulunmaktadır. \nEk hesabınızda {hesap['ek_hesap']} ₺ bulunmaktadır.")

para_cek(Baris_hesap, 3000)
print("*"*50)
para_cek(Baris_hesap, 2000)

        