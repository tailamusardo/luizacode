# O que fazer para criar uma função?
# A sintaxe de uma função é definida por três partes: nome, parâmetros e corpo, o qual agrupa uma sequência de linhas que representa algum comportamento.
# No código abaixo, temos um exemplo de declaração de função em Python que tem como objetivo imprimir o parâmetro passado.
# Uma função só é executada quando chamamos por ela, observe que não só criamos a função foo, como logo abaixo a chamamos passando o parâmetro.

from functools import reduce

def foo(value):
    print(f'Olá, esse é o parâmetro: {value}')

foo('LuizaCode')

# --/--

lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1 - 0.1)

# 1 - Dada uma lista com n valores, aplicar a função de desconto usando map()
# 2 - Retornar os valores maiores que 100, usando filter()
# 3 - Somar todos os valores da lista usando reduce()

desconto = map(lambda x: x-(x*0.1), lista)
print(list(desconto))

maior_100 = filter(lambda x: x > 100, lista)
print(list(maior_100))

soma = reduce(lambda x, y: x+y, lista, 0)
print(soma)