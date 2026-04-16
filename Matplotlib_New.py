import matplotlib.pyplot as plt
# %matplotlib inline # no necesitamos en show en otras versiones

numeros = [4, 2, 7, 9, 8]
# plt.plot(numeros) 

para guardar el gráfico   
plt.savefig(r"C:\Users\javie\OneDrive\Desktop\Excel_DB\mi_grafico.png");

plt.figure(facecolor="orange")
plt.plot(numeros)

plt.subplots(ncols=2, nrows=2)
plt.show()

fig, axs = plt.subplots(ncols=2, nrows=2)
print(type(fig), type(axs), axs[0])

print(axs[0][0]) # para poder llegar al primer recuadro

print(type(axs[0][0]))

axes1 = axs[0][0]
print(axes1.yaxis)
