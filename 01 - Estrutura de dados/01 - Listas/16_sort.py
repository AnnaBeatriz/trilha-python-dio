linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista por ordem alfabetica
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# Ordena e espelha a ordenação
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# Ordena por tamanho de caracter (do menor para o maior)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# Ordena por tamanho de caracter (do maior para o menor)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
