linguagens = ["python", "js", "c", "java", "csharp"]

# Ordem crescente e descrecente por tamanho de caracter de cada item da lista
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]


