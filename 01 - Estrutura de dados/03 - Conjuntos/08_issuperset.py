conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Todos os elementos de b estão em a? Sim
resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

# Todos os elementos de a então em b? Não
resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
