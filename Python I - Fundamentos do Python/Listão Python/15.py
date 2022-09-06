# 15). Para o programa Python no arquivo ex15.py: 
# Em uma casa, uma família decidiu dividir o valor da conta de energia entre os moradores da casa.
# No programa eles informam o valor da conta de energia e quantos que irão pagar a conta no mês.
# O programa calculará quanto cada um deverá contribuir com a conta de energia.

valor_conta = float(input("Qual o valor da conta? "))
pessoas = int(input("Quantas pessoas dividirão a conta? "))

valor_pessoa = valor_conta / pessoas

print (valor_pessoa)