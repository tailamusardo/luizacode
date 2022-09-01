# Entendo o que é List Comprehensions e porquê usá-las.
# Compreensão de listas foi concebida na PEP 202 e é uma forma concisa de criar e manipular listas.
# Basicamente é a forma mais rápida de criar uma lista através de outra.
# Python oferece diferentes formas de iteração, mas list comprehensions é mais otimizada para o interpretador python detectar um padrão previsível durante o loop, e como bônus ela é mais legível e economiza variáveis na contagem.

# Dada uma quantidade de n números, listar somente os números pares

# melhor prática
lista = [i for i in range(10) if i%2 == 0]
print(lista)

# prática não recomendada
i = 0
lista = []
while i < 10:
    if i%2 == 10:
        lista.append(i)
print(lista)