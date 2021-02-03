import pandas as pd
df = pd.read_csv("youtube-ing.csv")

# 1 - ilk 10 kaydı getiriniz
result = df.head(10)

# 2 - İkinci 5 kaydı getiriniz
result = df[5:].head()

# 3 - Dataset' de bulunan kolon isimlerini ve sayısını bulunuz
result = df.columns
result = len(df.columns)

# 4 - Aşagıda bulunan  bazı kolonları silin ve kalan kolonları listeleyiniz 
#       (thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed, description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"], axis = 1, inplace = True) ## axis = 1 kolonu siler
result = df

# 5 - Begenme (like) ve begenmeme (dislike) sayılarının ortalamasını bulunuz
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6 - ilk 50 videonun like ve dislikes kolonlarını getiriniz
result = df[:50][["likes","dislikes"]]
result = df.head(50)[["likes","dislikes"]]

# 7 - En çok görüntülenen video hangisidir ?
result = df[df["views"] == df["views"].max()]["title"].iloc[0]

# 8 - En düşük görüntelenen video hangisidir ?
result = df[df["views"] == df["views"].min()]["title"].iloc[0]

# 9 - En fazla görüntülenen video ilk 10 video hangisidir
result = df.sort_values("views", ascending = False).head(10)["title"]

# 10 - Kategoriye göre begeni ortalamalarını sıralı sekilde getiriniz
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11 - Kategoriye göre yorum sayılarını yukarıdan aşagıya dogru sıralyınız
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12 - Her kategoride kaç video vardır ?
result = df["category_id"].value_counts()

# 13 - Her videonun title uzunlugu bilgisini yeni bir kolonda gösteriniz
df["title_len"] = df["title"].apply(len)
result = df

# 14 - Her video için kullanılan tag sayısını yeni kolonda gösteriniz
df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")))

# 15 - En popüler videoları listeleyiniz (likes/dislikes oranına göre)
def oran_hesapla(dataset):
    likes_list = list(dataset["likes"])
    dislikes_list = list(dataset["dislikes"])
    liste = zip(likes_list, dislikes_list) ## tuple liste çevrildi (likes bilgisi, dislikes bilgisi)

    oran_listesi = []

    for like, dislike in liste:
        if(like + dislike) == 0:
            oran_listesi.append(0)
        else:
            oran_listesi.append(like /(like + dislike))

    return oran_listesi

df["begeni_oranı"] = oran_hesapla(df)

print(df.sort_values("begeni_oranı", ascending = False)[["title","likes","dislikes","begeni_oranı"]])