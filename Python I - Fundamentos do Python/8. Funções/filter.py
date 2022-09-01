# Filtrar
# filter() - Syntax filter(função, iteráveis)
# Utilizamos o filter() quando precisamos filtrar elementos da lista.

lista = [0,1,2,3,4,5,6,7,8,9]

pares = filter(lambda x: x%2 == 0, lista)
print(list(pares))