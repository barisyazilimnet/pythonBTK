# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print("Hello",name)

# # say_hello = my_decorator(say_hello)
# say_hello("Barış")

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time() # fonksiyonun başladıgı zamanı söler
        time.sleep(1) # 1 saniyelik bekler
        func(*args, **kwargs)
        finish = time.time() # donksiyonun durdupu zamanı söler
        print(f"{func.__name__} fonksiyonu {finish-start} saniye sürdü")
    return inner

@calculate_time
def us_alma(a,b):
    print(math.pow(a,b))
    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)
    
us_alma(2,3)
faktoriyel(5)
toplama(10,20)