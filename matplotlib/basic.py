import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = [1,2,3,4] ## x ekseni
# y = [1,4,9,16] ## y ekseni

# plt.plot(x,y, "o--r") ## grafikte çizgi oluşturmak için // "[birleşim noktasındaki oluşacak şekil][oluşacak cizginin şekli][oluşacak çizginin rengi]" //
# # // "o--r" // ## çizgi kısa kısa çizgiler halinde ve kırmızı olur x ve y ekseninin birleştigi noktalardada yuvarlak olur
# # // "--g" // ## çizgi kısa kısa çizikler halinde yeşil renkte olur
# # // "-g" // ## çizgi tek parça ve yeşil renkte olur 
# # // color = "red", linewidth = "5" // ## color cizgiye renk verir ## linewidth çizgi kalınlığı belirler
# plt.axis([0,6,0,20])  ## ilk ikisi x ekseninde denk gelecek ikinci iki y eksenine gelecek
# plt.title("Grafik başlığı") ## grafik başlıgı vermek için
# plt.xlabel("x ekseni") ## x eksenine isim vermek için
# plt.ylabel("y ekseni") ## y eksenine isim vermek için

# x = np.linspace(0,2,100)
# plt.plot(x,x, label = "linear", color = "red")
# plt.plot(x,x**2, label = "quadratic", color = "yellow")
# plt.plot(x,x**3, label = "cubic", color = "green")

# plt.xlabel("x label")
# plt.ylabel("y label")

# plt.legend() ## cizgilere verdigimiz isimler ve renkleri gösterir


# plt.show() ## grafigi göstermek için

# x = np.linspace(0,2,100)
# fig, axs = plt.subplots(3) ## fig == fügir alanı oluşturur ## axs = plt.subplots() kaç tane isteniyorsa axes alanı oluşturur

# axs[0].plot(x,x, color = "red") ## index numarasıyla axes lere ulaşıbalbilir
# axs[0].set_title("linear") ## grafiklere başlık verir

# axs[1].plot(x,x**2, color = "green")
# axs[1].set_title("quadratic")

# axs[2].plot(x,x**2, color = "green")
# axs[2].set_title("cubic")

# plt.tight_layout() ## grafikler arası boşlugu artırır

# x = np.linspace(0,2,100)
# fig, axs = plt.subplots(2,2)
# fig.suptitle("grafik başlıgı")

# axs[0,0].plot(x,x, color = "red") 
# axs[0,1].plot(x,x**2, color = "blue")
# axs[1,0].plot(x,x**3, color = "green")
# axs[1,1].plot(x,x**4, color = "yellow")


df = pd.read_csv("nba.csv")

df = df.drop(["Number"], axis = 1).groupby("Team").mean()
df.head().plot(subplots = True) ## grafikleri ayırır
plt.legend()
plt.show()