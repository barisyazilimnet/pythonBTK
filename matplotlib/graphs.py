import matplotlib.pyplot as plt

# # Stack Plot
# yil = [2011,2012,2013,2014,2015]
# oyuncu_1 = [8,10,12,7,9]
# oyuncu_2 = [7,12,5,15,21]
# oyuncu_3 = [18,20,22,25,19]

# plt.plot([],[],color = "y", label = "oyuncu1")
# plt.plot([],[],color = "r", label = "oyuncu2")
# plt.plot([],[],color = "b", label = "oyuncu3")

# plt.stackplot(yil, oyuncu_1, oyuncu_2, oyuncu_3, colors = ["y","r","b"])
# plt.title("Yıllara göre atılan goller")
# plt.xlabel("Yıl")
# plt.ylabel("Gol sayısı")
# plt.legend()
# plt.show()

# Pie plot
# goal_types = "Penaltı","Kaleye Atılan Şut","Serbest Vuruş"
# goals = [12,35,7]
# color = ["y","r","b"]

# plt.pie(goals, labels = goal_types, colors = ["y","r","b"], shadow = True, explode = (0.05,0.05,0.05), autopct = "%1.1f%%") 
# ## shadow => gölgelendirme / explode => grafikler arası boşluk / autopct => yüzdelik dilim gösterimi
# plt.show()

# Bar plot
# plt.bar([0.25,1.25,2.25,3.25,4.25], [50,40,70,80,20], label = "BMW", width =.5)
# plt.bar([0.75,1.75,2.75,3.75,4.75], [80,20,20,50,60], label = "Audi", width =.5)

# plt.legend()
# plt.xlabel("Gün")
# plt.ylabel("Alınan mesafe (km)")
# plt.title("Araç bilgileri")
# plt.show()

# histogram plot
yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar, yas_gruplari, histtype = "bar", rwidth = 0.8)
plt.xlabel("Yaş grupları")
plt.ylabel("Kişi sayısı")
plt.title("Histogram")

plt.show()