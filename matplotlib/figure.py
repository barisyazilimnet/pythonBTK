import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2

# figure = plt.figure()

# axs_cube = figure.add_axes([0.1,0.1,0.8,0.8]) ## axes alanın konumunu belirler [soldan saga getirir, alttan yukarı getirir, genişlik, yükseklik] axes alanın tamamı 1 dir
# ## [0.2,0.2,0.8,0.8] => soldan ve alttan %20 lik boşluk bırakır.
# ## [0.0,0.0,0.9,0.9] => sola ve alta tam yanaştırır. axes alanıda %90 alan kaplar
# axs_cube.plot(x,y,"b")
# axs_cube.set_xlabel("x ekseni")
# axs_cube.set_ylabel("y ekseni")
# axs_cube.set_title("Cube")

# axs_square = figure.add_axes([0.15,0.6,0.25,0.25])
# axs_square.plot(x,z,"r")
# axs_square.set_xlabel("x ekseni")
# axs_square.set_ylabel("y ekseni")
# axs_square.set_title("Square")

# axs = figure.add_axes([0,0,1,1])
# axs.plot(x,y,label = "Cube")
# axs.plot(x,z,label = "Square")
# axs.legend(loc = 4) 
# ## 1 => sag üstte
# ## 2 => standart olan sol üstte
# ## 3 => sol altta
# ## 4 => sag altta

fig,axs = plt.subplots(nrows = 2, ncols = 1, figsize = (8,8))
axs[0].plot(x,y)
axs[0].set_title("Cube")
axs[1].plot(x,z)
axs[1].set_title("Square")

plt.tight_layout()
fig.savefig("Figure1.pdf") ## png / pdf
plt.show()
