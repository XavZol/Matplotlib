import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\javie\OneDrive\Desktop\Excel_DB\Ventas.csv")
print(df)

plt.hist(df['Producto'])
plt.show()

numeros = np.random.randn(1000)
print(numeros)

plt.hist(numeros)
plt.show()

plt.hist(numeros, bins=40, alpha=0.5, color='red')
plt.show();

plt.hist(numeros, bins=40, alpha=0.5, color='red', edgecolor='green', histtype='step')
plt.show();


x1 = np.random.randn(1000)
x2 = np.random.randn(500)
x3 = np.random.randn(100)
plt.hist(x1, histtype='stepfilled', alpha=0.3, bins=40)
plt.hist(x2, histtype='stepfilled', alpha=0.3, bins=40)
plt.hist(x3, histtype='stepfilled', alpha=0.3, bins=40)
plt.show();