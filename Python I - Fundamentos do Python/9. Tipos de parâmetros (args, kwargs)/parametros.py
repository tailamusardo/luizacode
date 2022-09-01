# Parâmetros são os nomes dados aos atributos que uma função pode receber, são eles que definem quais são os argumentos aceitos por uma função, podendo ou não ter um valor padrão.
# Temos aqui um exemplo de uma função recebendo dois parâmetros, um de valor que é obrigatório e um de horas, que não é obrigatório porque tem um valor padrão, porém pode ser modificado se informado.

def calcula_salario(valor, horas=220):
    return valor * horas

print(calcula_salario(35))

# *args e **kwargs
# As palavras args e kwargs são apenas usadas como convenção, poderia receber qualquer outro nome: *params, **kparams, por exemplo.

# *args é usado para passar uma lista de argumentos variável sem palavras chaves em forma de tupla, pois a função que recebe não necessariamente saberá quantos argumentos serão passados.

def foo(*args):
    print(f'conteudo: {args}')

    for i in args:
        print(i)

foo('Hello', 'Moças', 'LuizaCode')

# … e **kwargs:
# É a abreviação de keyword arguments, ele permite passar um dicionário com inúmeras chaves para a função.
# Isso deixa definido que tal função irá receber tais valores, pronto.

def foo(*kwargs):
    print(f'O nome dela(e) é: {kwargs.get("nome")}')

foo(nome='João',
    idade='26',
    país='Brasil')