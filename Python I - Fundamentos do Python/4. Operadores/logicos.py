# Python nos disponibiliza três tipos de Operadores Lógicos: o and, o or e o not.

# Operador        Definição
# and             Retorna True se ambas afirmações forem verdadeiras
# or              Retorna True se uma das afirmações for verdadeira
# not             Retorna falso se o resultado for verdadeiro

num1 = 7
num2 = 4

if num1 > 3 and num2 < 8:
    print('As duas condições são verdadeiras')

if num1 > 4 or num2 <= 8:
    print('Uma ou duas das condições são verdadeiras')

if not (num1 > 30 and num2 > 8):
    print('Inverte o resultado da condição entre os parâmetros')

lista = ['a', 'b', 'c', 'd'] 
if 'e' not in lista:
    print('não tem o e na lista')