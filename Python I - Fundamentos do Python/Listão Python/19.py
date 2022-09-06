# 19). Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a venda for …
# ● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
# ● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da venda;
# ● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
# ● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
# ● acima de R$50.000,00 a comissão será de 30% da venda.
# Faça um programa que informe o valor da comissão do vendedor para uma venda.

venda = float(input("Informe o valor da venda: "))

if venda < 1000:
    print("Sem comissão")
elif venda >= 1000 or venda < 5000:
    print(f'O valor da comissão é {venda * 0.1}')
elif venda >= 5000 or venda < 10000:
    print(f'O valor da comissão é {venda * 0.2}')
elif venda >= 10000 or venda < 50000:
    print(f'O valor da comissão é {venda * 0.25}')
else:
    print(f'O valor da comissão é {venda * 0.3}')