lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
# Posição colocada -1
print(lista[:2])  # ["p", "y"]
# tudo que e passado no final como posição vai ser -1
print(lista[1:3])  # ["y", "t"]
# terceiro campo é a quantidade de que os campos vão pular
# truxe p e pulo dois campos da lista e trouxe o t
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
