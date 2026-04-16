import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "etiquetas": ['Manzanas', 'Bananas', 'Naranjas', 'Uvas'],
    "cantidad":[30, 60, 80, 20]
})
print(df)

plt.pie(df['cantidad']);
plt.show()

plt.pie(df['cantidad'], 
        labels=df['etiquetas'],
        autopct='%1.1f%%',
        colors=['#87CEEB', '#6495ED', '#000080', '#40E0D0'])
plt.show()

plt.pie(df['cantidad'], 
        labels=df['etiquetas'],
        autopct='%1.1f%%',
        colors=['#87CEEB', '#6495ED', '#000080', '#40E0D0'],
        shadow=True,
        explode=(0,0,0, 0.5))
plt.title("Mis Frutas") 
plt.show()