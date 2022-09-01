# Mapear
# map() - Syntax map(função, iteráveis)
# Utilizamos esta função quando precisamos realizar uma operação específica nos itens da lista e transformá-los em outra coisa.

lista = [0,1,2,3,4,5,6,7,8,9]

lista_somada = map(lambda x: x+x, lista)
print(list(lista_somada))