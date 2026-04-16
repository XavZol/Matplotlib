import pandas as pd
import matplotlib.pyplot as plt

# plt.style.use('ggplot')

fig = plt.figure
ax = plt.axes()

print(ax)

x = [1, 2, 3, 5, 6, 8, 9, 7]
y = [1, 6, 3, 4, 8, 7, 6, 7]
plt.plot(x, y, "b*:")
plt.grid()
plt.show()

# help(plt.axis)

x = [1, 2, 3, 5, 6, 8, 9, 7]
y = [1, 6, 3, 4, 8, 7, 6, 7]
plt.plot(x, y, "ro-")
plt.axis([0, 10, 0, 10])
plt.grid()
plt.show()


ruta = r"C:\Users\javie\OneDrive\Desktop\Excel_DB\Lluvias_region_A.csv"
df = pd.read_csv(ruta)
print(df)

plt.plot(df['region'],df['enero'])
plt.grid()
plt.show()

plt.plot(df['region'],df['enero']) # Rotación en 45 grados para mejor presentación
plt.xticks(rotation=45)
plt.grid()
plt.show()