# Reduzir
# reduce() - Syntax reduce(função, iteráveis)
# Esta função aplica uma operação em todos os elementos da lista reduzindo a apenas um elemento.
# Agora, diferente das outras duas, essa função não é diretamente do interpretador, precisamos importar o módulo functools.

from functools import reduce

#Somar os ites da lista
lista = [0,1,2,3,4,5,6,7,8,9]
soma = reduce(lambda x, y: x+y, lista, 0)
print(soma)