# É importante saber como manusear uma lista, em python temos vários métodos que estão disponíveis para nos ajudar nisso, confira comigo alguns deles:

# ● list.append(x): adiciona um item ao fim da lista
# ● list.extend(iterable): adiciona todos os itens do iterável ao fim da lista
# ● list.insert(i, x): insere um item em uma dada posivel (i) dada pelo index
# ● list.remove(x): remove o primeiro elemento cujo o valor for “x”
# ● list.pop(i): remove o item da posição i da lista e retorna, caso o index não seja especificado, retona o último elemento.
# ● list.clear(): remove tudo da lista
# ● list.index(x[, start[, end]]): retorna o indice do primeiro elemento cujo valor seja x.
# ● list.count(x): retorna o número de vezes que x aparece na lista
# ● list.sort(key=nome, reverse=False): ordena os itens da lista
# ● list.reverse(): reverte os elementos da lista
# ● list.copy(): retorna uma lista com a cópia dos elementos da lista de origem.


lista = [0,5,8,10,35,15,7,4,12,22,3,2,9,1]
list_appened = []

for i in lista:
    list_appened.append(i+1)

print(f'Appened: {list_appened}')

list_appened.extend([0,0,0,0])
print(f'Extend: {list_appened}')

list_appened.insert(8, 'meio')
print(f'Insert: {list_appened}')

list_appened.remove('meio')
print(f'Remove: {list_appened}')

list_appened.pop(4)
print(f'Pop: {list_appened}')

print(f'Index: {list_appened.index(11)}')

list_appened.sort()
print(f'Sort: {list_appened}')

list_appened.reverse()
print(f'Reverse: {list_appened}')

list_new = list_appened.copy()
print(f'Copy: {list_new}')