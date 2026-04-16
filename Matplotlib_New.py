import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace( 0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o') # Gráfico Scatter
plt.show();

aleatorio = np.random.RandomState(0)
marcadores = ['o', 'x', '+', 'v', 's', 'd']
for marcador in marcadores: 
    plt.plot(aleatorio.rand(5), aleatorio.rand(5), marcador)
    plt.show()
    
plt.plot(x,y , ':ob')
plt.show()

plt.plot(x, y, '-p')
plt.show()

plt.plot(x, y, '-p' ,color='red', markersize=15, linewidth=2, markerfacecolor='white')
plt.show()

plt.scatter(x, y)
plt.show()

aleatorio1 = np.random.RandomState(0)
plt.scatter(aleatorio1.randn(100),
            aleatorio1.randn(100),
            c=aleatorio1.randn(100),
            s=aleatorio1.randn(100) * 1000,
            alpha=0.3,
            cmap='viridis')
plt.colorbar()
plt.show()
