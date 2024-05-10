contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# Se o atibuto não tiver no dicionario e ele adiciona
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# Se o atributo tiver no dicionario ele não altera
contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
