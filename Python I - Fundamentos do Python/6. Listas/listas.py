# Uma lista, nada mais é que uma coleção ordenada de valores, onde cada valor é identificado por índices. Em Python representamos uma lista separando os dados por vírgula, dentro de colchetes.
# Elas são utilizadas para armazenar diversos itens em uma única variável e existem várias maneiras de serem criadas.

# letters = ["a", "b", "c"]

# Como acessar os dados de uma lista?
# Todos os itens de uma lista são indexados, ou seja, para cada item da lista um índice é atribuído ao mesmo, para acessar esses itens é necessário que especifiquemos o índice, lembrando, o índice começa no 0.

# letters = ["a", "b", "c"]
#             0    1    2

# Podemos criar uma lista de uma maneira bem simples, apenas envolvendo os elementos por colchetes:

lista = ['luizacode']
print(type(lista))

# lista vazia

lista = []

# Também é possível criar uma lista com vários itens e de diferentes tipos:

lista = ['luizacode', 5, 'python']

# Podemos obter uma lista através de compreensão de listas (List Comprehensions)

# [item for item in iteravel]

# Acessar os dados de uma lista

lista = ['maça', 'banana', 'jaca', 'melão', 'abacaxi']
print(f'Estou fuscando a Fruta: {lista[2]}')

# E para pegar o último item da lista?
# Uma forma de buscar o último item, ou itens mais próximos ao fim, é usando  indexação negativa.
# A indexação negativa, vai buscar os itens do fim, logo, se eu quiser buscar o Abacaxi de uma forma mais simples, basta fazer assim:

print(f'Estou fuscando a Fruta: {lista[-1]}')