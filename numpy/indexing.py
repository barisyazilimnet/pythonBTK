import numpy as np 

numbers = np.array([0,5,10,15,20,25,50,75])
# result = numbers[5] # 5. indexdeki degeri yazdırır
# result = numbers[-1] # sondan 1. indexdeki degeri yazdırır
# result = numbers[0:3] # 0 ile 3. index arasındaki degerleri alır
# result = numbers[:3] # 0 ile 3. index arasındaki degerleri alır
# result = numbers[3:] #3. indexden sonra ki bütün degerleri alır
# result = numbers[::] # büütn listeyi verir
# result = numbers[::-1] # listeyi ters çevirir
# result = numbers[::-2] # listeyi ters çevirir ve ve bir bir atlayarak gider

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
# print(numbers2)
# result = numbers2[0] # 0. indexdeki degeri veya degerleri verir
# result = numbers2[0,2] # 0. indexin 2. indexinde olan elemanı verir
# result = numbers2[2,2] # 2. indexin 2. indexinde olan elemanı verir
# result = numbers2[:,2] # bütün satırlardaki 2. indexi verir
# result = numbers2[:,0:2] # bütün satırlardaki 0 ile 2. index arasındaki degerleri verir
# result = numbers2[-1,:] #  sondan 1. indexdeki degerleri veya degeri alır
result = numbers2[:2,:2] # ilk 2 satırdaki ilk 2 elemanı alır

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1
arr2 = arr1.copy()
arr2[0] = 20 
print(arr1)
print(arr2)


