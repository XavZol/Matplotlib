import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame({
    "etiquetas":['Manzanas', 'Bananas', 'Naranjas', 'Uvas'],
    "cantidad":[30,35, 26,33]
})

print(df)

fig, axs = plt.subplots(ncols=2, nrows=1)
axs1 = axs[0]
axs2 = axs[1]
axs1.plot(df['etiquetas'], df['cantidad'])
axs2.pie(df['cantidad'])
plt.show()

plt.style.use('ggplot')

fig, axs = plt.subplots(ncols=2, nrows=1)
axs1 = axs[0]
axs2 = axs[1]
axs1.plot(df['etiquetas'], df['cantidad'])
axs2.pie(df['cantidad'])
plt.show()

print(plt.style.available)

plt.style.use('seaborn-v0_8-pastel')

fig, axs = plt.subplots(ncols=2, nrows=1)
axs1 = axs[0]
axs2 = axs[1]
axs1.plot(df['etiquetas'], df['cantidad'])
axs2.pie(df['cantidad'])
plt.show()