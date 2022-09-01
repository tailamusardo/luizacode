# Diferente da conversão Implícita, esse tipo de conversão é feita manualmente pelo usuário de acordo com seus requisitos, existem várias formas de conversão que se pode fazer nesse tipo, usando as funções do Python:

# https://docs.python.org/3/library/functions.html

# ● int(a, base): essa função converte qualquer tipo de dado em inteiro. ‘Base’  especifica a base em que a string está se o tipo de dados for uma string
# ● float(): função usada para converter qualquer tipo de dados em um float, literalmente.
# ● str(): usada para converter números inteiros em strings
# ● dict(): usada para converter tuplas em dicionário
# ● ord(): função usada para converter qualquer caractere em um inteiro
# ● hex(): função que converte número inteiro em uma string hexadecimal*
# ● oct(): converte um número inteiro em octal
# ● tupla: converte para uma tupla

a = 1
print(type(a))

a = str(a)
print(type(a))

a = tuple(a)
print(type(a))