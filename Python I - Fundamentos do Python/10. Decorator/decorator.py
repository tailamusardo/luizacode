# Lá na PEP 318, veio a proposta de melhoria na linguagem, que propôs o decorator, que nada mais é do que um método para envolver uma função, modificando o seu comportamento.

# Dá um olhada no código abaixo, que tem a seguinte saída:
# >>> Estou antes da execução da função passada como argumento
# >>> Sou um belo argumento
# >>> Estou depois da execução da função passada como argumento

def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print 
        ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()

# Usando decorator conseguimos adicionar qualquer comportamento antes e depois da execução de uma função qualquer.
# Podemos usar o decorator com o @, que fará o mesmo papel de como se estivessemos chamando a função da imagem anterior, mostrarei um exemplo útil de utilização de decorator, colocando o @ em cima da função que será decorada.

import time

def calcula_tempo(funcao):
    def wrapper():
        tempo_inicio = time.time()
        funcao()
        tempo_final = time.time()

        calculo = tempo_final - tempo_inicio

        print (f'A {funcao.__name__}, levou o total de {calculo} para ser executada')

    return wrapper

@calcula_tempo
def run():
    for n in range(100000000000):
        yield

run()
    

