# 16). Programa ex16.py: Estou tentando entender os juros do meu banco. Para isto, ele me # informou esta fórmula:
# valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
# onde que:
# ● valor_emprestimo: É o valor que pegarei emprestado.
# ● taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
# ● tempo: Quantidade de meses que irei pagar o empréstimo.
# Crie um programa que colete cada um destes valores para calcular o valor final que estarei # pagando ao banco.

valor_emprestimo = float(input("Qual o valor emprestado? "))
taxa = int(input("Qual a % da taxa mensal? "))
tempo = float(input("Por quantos meses emprestarei o dinheiro? "))

taxa = taxa / 100

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)

print (valor_final)