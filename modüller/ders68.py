#datetime
import datetime

# result = datetime.datetime.now() #tarih ve saat ayrıntılı gelir
# result = datetime.datetime.today() aynı üstteki ayrıntılı bilgi verir
# result = datetime.datetime.now().year  sadece yıl bilgisini alır
# result = datetime.datetime.now().month sadece ay bilgisini alır
# result = datetime.datetime.now().day sadece gün bilgisini alır
# result = datetime.datetime.now().hour sadece saat kısmını alır dakikayı almaz
# result = datetime.datetime.now().minute sadece dk bilgisini alır
# result = datetime.datetime.now().second sadece saniye bilgisini alır
# result = datetime.datetime.ctime(result) # gün adını ve ay adını yazılı şekilde biraz daha açıklayıcı bir biçimde yazar
# result = datetime.datetime.strftime(result, "%y") #sadece yıl(kısaltılmış) bilgisini verir eger büyük yazılırsa tam yıl bilgisini verir
# result = datetime.datetime.strftime(result, "%X") #saat dk ve saniye bilgisini verir ve eger küçük olarak yazılırsa adece gün/ay/yıl(kısaltılmış) bilgisini sayılsal verir
# result = datetime.datetime.strftime(result, "%D") #sadece gün/ay/yıl(kısaltılmış) bilgisini sayılsal verir eger küçük d yazılırsa sadece gün bilgisini sayısal verir
# result = datetime.datetime.strftime(result, "%A") gün ismini verir eger küçük a olursa kısaltılmış halde verir
# result = datetime.datetime.strftime(result, "%b") ay bilgisini verir büyük yazılsada fark etmez
# result = datetime.datetime.strftime(result, "%a %b %y")
# time ="15 April 2019 hour 10:12:30"
# result = datetime.datetime.strptime(time,"%d %B %Y hour %H:%M:%S")
# result = result.year
now = datetime.datetime.now()
# birthday = datetime.datetime(2000,1,30,12,30,10)
# result = datetime.datetime.timestamp(birthday) # tarihi saniyeye çevirir
# result = datetime.datetime.fromtimestamp(result) # saniyeye tarihe çevirir
# result = now -birthday
# # result = result.days
# # result = result.seconds
# result = result.microseconds
print(now)
# result = now + datetime.timedelta(days=365)
# result = now + datetime.timedelta(days=750, minutes=15)
result = now - datetime.timedelta(days=15)

print(result)