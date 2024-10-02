
squares = []
for x in range(10):
    squares.append(x**2)


squares = [x**2 for x in range(10)]
print("Cuadrados:", squares)


even_numbers = []
for x in range(20):
    if x % 2 == 0:
        even_numbers.append(x)


even_numbers = [x for x in range(20) if x % 2 == 0]
print("Números pares:", even_numbers)

words = ['hello', 'world', 'python']
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())


uppercase_words = [word.upper() for word in words]
print("Palabras en mayúsculas:", uppercase_words)

pairs = []
for x in range(3):
    for y in range(3):
        pairs.append((x, y))


pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pares (x, y):", pairs)
