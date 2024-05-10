conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Todos os elementos de a pertencem a b? Sim
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

# Todos os elementos de b pertencem a a? Não
resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)
