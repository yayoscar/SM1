import matplotlib.pyplot as plt

# Primeros cinco números cúbicos
x1 = [1, 2, 3, 4, 5]
y1 = [i**3 for i in x1]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x1, y1, marker='o')
plt.title('Primeros cinco números cúbicos')
plt.xlabel('Número')
plt.ylabel('Cubo')
plt.grid()

# Primeros 5000 números cúbicos
x2 = list(range(1, 5001))
y2 = [i**3 for i in x2]

plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title('Primeros 5000 números cúbicos')
plt.xlabel('Número')
plt.ylabel('Cubo')
plt.grid()

plt.tight_layout()
plt.show()
