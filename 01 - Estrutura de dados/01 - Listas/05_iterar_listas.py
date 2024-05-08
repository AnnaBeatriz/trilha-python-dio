carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


# Para saber o indice que está percorrendo dentro da lista
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
