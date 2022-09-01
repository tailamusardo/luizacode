# Percorrendo uma lista
# Se precisarmos percorrer uma lista, a melhor forma é usarmos loop.
# Por exemplo, dada uma lista grande de elementos, eu quero buscar somente aqueles que forem maior que 10:

lista = [0,5,8,10,35,15,7,4,12,22,3,2,9,1]

lista_numero_maior_10 = []

for i in lista:
    if i > 10:
        lista_numero_maior_10.append(i)

print(f'Resultado da lista: {lista_numero_maior_10}')

# Também pode ser feito assim:

lista_numero_maior_10 = [i for i in lista if i > 10]
print(f'Resultado da lista: {lista_numero_maior_10}')