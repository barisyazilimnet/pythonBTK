import pandas as pd
df = pd.read_csv("imdb.csv")

# 1 - Dosya hakkındaki bilgiler
result = df

# 2 - İlk 5 kaydı gösterin
result = df.head()

# 3 - İlk 10 kaydı gösterin
result = df.head(10)

# 4 - Son 5 kaydı gösterin
result = df.tail()

# 5 - Son 10 kaydı gösterin
result = df.tail(10)

# 6 - Sadece Movie_Title kolonunu alın
result = df["Movie_Title"]

# 7 - Sadece Movie_Title kolonunu içerren ilk 5 kaydı alın
result = df["Movie_Title"].head()

# 8 - Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın
result = df[["Movie_Title","Rating"]].head()

# 9 - Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın
result = df[["Movie_Title","Rating"]].tail(7)

# 10 - Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın
result = df[5:][["Movie_Title","Rating"]].head()

# 11 - Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alınız
result = df[["Movie_Title","Rating"]][df["Rating"] >= 8.0].head(50)

# 12 - Yayın Tarihi 2014 ve 2015 arasında olan filmlerin isimlerini getiriniz
result = df.columns ## kolon bilgileri için
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]]

# 13 - Değerlendirme sayısı (Num_Reviews) 100.000 den büyük yada imdb puanı 8 ile 9 arasında olan filmleri listeyiniz
result = df[(df["Num_Reviews"] > 100000) | ((df["Rating"] >= 8.0) & (df["Rating"] <= 9.0))][["Movie_Title","Num_Reviews","Rating"]]

print(result)