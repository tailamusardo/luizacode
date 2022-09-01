# Na conversão implícita, acontece do interpretador converter automaticamente um tipo de dado em outro sem qualquer envolvimento do usuário.

a = 15
print(f'A variável a é do tipo: {type(a)}')

b = 10.6
a = a+b
print(f'Valor da soma: {a}')

print(f'A variável a é do tipo: {type(a)}')