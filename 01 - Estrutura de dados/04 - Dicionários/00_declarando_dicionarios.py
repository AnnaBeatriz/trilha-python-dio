# Pode ser um objeto imutavel ou mutavel
# São pares
# Definir chave(nome) e valor(Guilherme)
# Pode usar tanto chaves {} quando o construtor dict
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

pessoa["nome"] = "Maria"
print(pessoa)