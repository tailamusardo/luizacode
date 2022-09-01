# Funções lambdas são como todas as outras: funções normais.
# Exceto pelo fato de não ter um nome para defini-la e estar contida em uma linha de código.
# A sintaxe é assim:

# lambda argument(s): expression

# Uma função lambda funciona da seguinte forma: você dá à função um valor (argumento) e então fornece a operação (expressão).
# A palavra lambda vem na frente, depois vem “:” e o argumento.

# Quais são os prós de usá-las?
# ● Bom para operações lógicas simples que são fáceis de entender, isso torna o código mais legível também
# ● Bom para funções que serão usadas apenas uma vez.

# E os contras?
# ● Elas só podem executar uma única expressão, por isso tem que ser usada somente no simples
# ● Se a função abrange mais de uma linha, esquece, não funcionará
# ● Dependendo do contexto ela vai ser executada somente uma

# Usei em slides anteriores a função lambda para facilitar os resultados, nas compreensões de lista, nas funções de filter, map, reduce.
# Contudo, vou mostrar um exemplo que deixa claro como podemos reduzir uma função simples, que busca os valores pares de uma lista, em uma linha.

lista = [1,2,3,4,5,6,7,8,9]

# Opção que funciona, porém não é muito recomendada
pares = []
def func_par():
    for i in lista:
        if i%2==0:
            pares.appened(i)
        return pares

print(func_par())

# Melhor prática

print(list(filter(lambda x: x%2==0, lista)))

# Funções lambdas por não ser nomeadas, são funções que chamamos de anônimas.
# Outro exemplo para fixar

lista2 = [1,2,3,4,5]

print(list(map(lambda x: x ** 2, lista2)))
