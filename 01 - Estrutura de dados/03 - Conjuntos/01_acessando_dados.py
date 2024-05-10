# Chave {} pode substituir a palavra set
# Não é possivel acessar os valores do set
# para acessar os valores do set é necessario converter para uma lista
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
