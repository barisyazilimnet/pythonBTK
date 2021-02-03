import pandas as pd
import numpy as np

personeller = {
    "Çalışan" : ["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    "Departman" : ["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
    "Yaş" : [30, 25, 45, 50, 23, 34, 42],
    "Semt" : ["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
    "Maaş" : [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}
df = pd.DataFrame(personeller)
result = df
result = df["Maaş"].sum() ## personellerin maaşları toplamı
result = df.groupby("Departman").groups ## gruplanlamarı ve kaçıncı indexde olduklarını gösterir
result = df.groupby(["Departman","Semt"]).groups

semtler = df.groupby("Semt") ## semtlere göre gruplandırır

# for name, group in semtler:
#     print(name)
#     print(group)


# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Muhasebe")
result = df.groupby("Departman").sum() ## departmana göre gruplanıp yaş ve maaş toplamları verilir
result = df.groupby("Departman")["Maaş"].mean() ## departmana göre gruplanıp maaş ortalaması hesaplanır
result = df.groupby("Semt")["Çalışan"].count() ## semte göre gruplanıp çalışan sayısı hesaplanır
result = df.groupby("Departman")["Maaş"].mean()["Muhasebe"] ## departmana göre gruplanıp muhasebe grubunun maaş ortalaması hesaplanır
result = df.groupby("Departman").agg(np.mean)
result = df.groupby("Departman")["Maaş"].agg([np.mean, np.sum, np.max, np.min]).loc["Muhasebe"]

print(result)