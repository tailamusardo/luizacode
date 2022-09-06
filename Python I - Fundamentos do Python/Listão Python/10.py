# 10) Crie o seguinte programa Python no arquivo lista03_02.py:
# Colete o nome da pessoa, a cidade de nascimento dela, e o ano em que ela nasceu.
# Depois você irá mostrar os dados coletados em linhas diferentes.
# E também, deverá informar quantos anos a pessoa terá no ano 2030.

nome_pessoa = input("Qual seu nome? ")
cidade_nascimento = input("Que cidade você nasceu? ")
ano_nascimento = int(input("Que ano você nasceu? "))

print (f'Nome: {nome_pessoa} \nCidade: {cidade_nascimento} \nAno de Nascimento: {ano_nascimento} \nSua idade em 2030: {2030 - ano_nascimento}')