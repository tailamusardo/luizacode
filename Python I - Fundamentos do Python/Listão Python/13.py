# 13). Crie o seguinte programa Python no arquivo ex13.py: Colete a idade de 3 pessoas e
# mostre a média de suas idades.

idade1 = int(input("Qual sua idade pessoa 1? "))
idade2 = int(input("Qual sua idade pessoa 2? "))
idade3 = int(input("Qual sua idade pessoa 3? "))

media_idades = (idade1+idade2+idade3)/3

print (
    "A média das idades é: ",
    media_idades
    )