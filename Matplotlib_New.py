import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\javie\OneDrive\Desktop\Excel_DB\Iluminacion.csv")
print(df)

# help(plt.hexbin)

fig, axs = plt.subplots()
hb = axs.hexbin(df['Latitud'], df['Longitud'], C=df['Luminosidad'], gridsize=50, cmap='Blues')
axs.set_facecolor('#D2F2FF')
plt.colorbar(hb, label="nivel de sombras")
plt.xlabel("Latitud")
plt.ylabel("Longitud")
plt.title("Luminosidad en Valle")
axs.set(xlim=(-4, 4), ylim=(-5,5))
plt.show()
