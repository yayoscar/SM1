import matplotlib.pyplot as plt

# Generar los primeros cinco números cúbicos
x_5 = list(range(1, 6))
y_5 = [n**3 for n in x_5]

# Generar los primeros 5000 números cúbicos
x_5000 = list(range(1, 5001))
y_5000 = [n**3 for n in x_5000]

# Crear la figura y los subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Graficar los primeros cinco números cúbicos
axs[0].plot(x_5, y_5, marker='o')
axs[0].set_title('Primeros 5 números cúbicos')
axs[0].set_xlabel('Número')
axs[0].set_ylabel('Cubo del número')

# Graficar los primeros 5000 números cúbicos
axs[1].plot(x_5000, y_5000, marker='.')
axs[1].set_title('Primeros 5000 números cúbicos')
axs[1].set_xlabel('Número')
axs[1].set_ylabel('Cubo del número')

plt.tight_layout()
plt.show()