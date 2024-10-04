# Ejemplo 1: Crear una lista de cuadrados
# Forma larga
squares = []
for x in range(10):
    squares.append(x**2)

# Comprensión de lista
squares = [x**2 for x in range(10)]
print("Cuadrados:", squares)

# Ejemplo 2: Filtrar números pares
# Forma larga
even_numbers = []
for x in range(20):
    if x % 2 == 0:
        even_numbers.append(x)

# Comprensión de lista
even_numbers = [x for x in range(20) if x % 2 == 0]
print("Números pares:", even_numbers)

# Ejemplo 3: Convertir una lista de cadenas a mayúsculas
# Forma larga
words = ['hello', 'world', 'python']
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())

# Comprensión de lista
uppercase_words = [word.upper() for word in words]
print("Palabras en mayúsculas:", uppercase_words)

# Ejemplo 4: Crear una lista de pares (x, y)
# Forma larga
pairs = []
for x in range(3):
    for y in range(3):
        pairs.append((x, y))

# Comprensión de lista
pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pares (x, y):", pairs)
