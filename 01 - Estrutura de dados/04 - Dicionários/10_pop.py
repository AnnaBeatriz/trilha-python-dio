contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Remove o valores
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# Utilizar quando precisa remover, mas não sabe se o valor ainda está na chave
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
