import matplotlib.pyplot as plt
import pandas as pd


fig, axs = plt.subplots(ncols=2, nrows=1)
axs1 = axs[0]
axs2 = axs[1]

axs1.plot([1, 2, 3, 4], [1, 4, 6, 8])
axs2.scatter([1, 2, 3, 4], [1, 4, 6, 8])

axs1.set_title("Gráfico de Línea")
axs2.set_title("Gráfico Scatter")
plt.show()