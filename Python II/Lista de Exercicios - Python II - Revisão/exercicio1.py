# 1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
# classe onde teremos o retorno do documento, o retorno do nome e
# verificação de tipo de pessoa, onde um método irá receber como
# parâmetro “F” ou “N” para trazer fumante ou não fumante.
# Feito isso, crie uma instância e retorne esses valores.

# pessoa = input("A pessoa é: ")
# cpf = input("Insira o CPF: ")
# nome = str(input("Insira o nome: "))
# idade = int(input("Insira a idade: "))

class Pessoa:

    def __init__(self, cpf, nome, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        
    def dados(self):
        return f'CPF: {self.cpf}, Nome: {self.nome}, Idade: {self.idade} anos'
        
    def fumante(self, fumante):
        if fumante == 'F':
            return f'Essa pessoa é fumante.'
        return f'Essa pessoa não é fumante'
