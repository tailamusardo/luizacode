# 5) Resolva estes problemas em Python, guardando os valores e seus resultados em variáveis diferentes.
# a. Calcule a área de um quadrado cujo lado seja 2 cm.
a = 2*2
# b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela.
b = 120-(120*0.05)
# c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem será 200 Km. Quantas horas irá demorar a viagem.
c = 200/100
# d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e sua média.
d = (2+3+1)/3
# e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a verificação se a idade de Davi é maior que a idade de sua irmã.
davi = 13
irma = 7

print(a)
print(b)
print(c)
print(d)

if davi > irma:
    print('eh_mais_velho')