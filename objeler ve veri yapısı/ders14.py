numbers =[1,10,5,16,4,9,10]
letters =["a","g","s","b","y","a","s"]

result = max(numbers) # maximum değeri yazdırır
result = min(numbers) # minimun değeri yazdırır
result = min(letters) # alfabede en başa yakın değeri alır
result = max(letters) # alfabede en sona yakın değeri alır
result = numbers[3:6]
result = letters[3:7]
numbers[4] = 40
numbers.append(49) # listeye 49 ekle listenin en sonuna ekler
numbers.insert(3,78) # listenin 3. indeksine 78 i ekler
numbers.pop() # en sondaki değeri siler
numbers.pop(3) #3. indeksi siler
# numbers.remove(49) # 49 değerini siler
numbers.sort() #küçükten büyüğe sıralar
letters.sort() # alfabenin ilk harfinden son harfine doğruna doğru sıralar
numbers.reverse() # listeyi tam tersine çevirir
letters.reverse()
result = letters
result =len(numbers)
result =len(letters)
result =numbers.count(10)
result =letters.count("a")
result =numbers.clear() # Listenin elemanlarını temizler
print(result)