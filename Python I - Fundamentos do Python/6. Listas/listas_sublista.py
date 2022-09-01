# Lista dentro de lista?
# Sim, é possível! Assim como no exemplo, para acessarmos a sub-lista é necessário que busquemos onde o índice da mesma está
#                    1         2 
lista = ['maça', ['banana', 'jaca'], 'melão', 'abacaxi']
#          0               1            2         3

sublista = lista[1]
print(f'Acessar sublista: {sublista}')

# Acessando um item da sublista

print(f'Acessar um item da sublista: {sublista[0]}')