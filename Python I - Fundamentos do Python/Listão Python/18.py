# 18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um
# valor inteiro entre zero e 100. Se o valor não estiver neste intervalo, informe que a
# nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso
# contrário, informa que ele foi reprovado.

nota = float(input("Informe a nota do aluno: "))

if nota > 100 or nota < 0:
    print("Nota inválida")
if nota > 60:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")