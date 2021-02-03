# def say_hello(name ="user"):
#     return "Hello " + name

# msg = say_hello("Barış")
# print(msg)

# def total(num1,num2):
#     print(num1 + num2)

# total(10,20)

def yas_hesapla(dogum_yili):
    return 2019 - dogum_yili

def emeklilige_kac_yil_kaldi(dogum_yili, isim):
    '''
    DOCSTRING: Dogum yiliniza göre emekliliginize kaç yıl kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yas_hesapla(dogum_yili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliginize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emekli oldunuz")

emeklilige_kac_yil_kaldi(2000, "Barış")

print(help(emeklilige_kac_yil_kaldi))