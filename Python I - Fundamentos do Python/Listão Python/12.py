# 12) Programa Python no arquivo ex12.py: Este programa irá calcular a área de um
# triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois
# colete o valor da altura. Apresente o valor da área do triângulo.

base_triangulo = float(input("Informe a base do triângulo: "))
altura_triangulo = float(input("Informe a altura do triângulo: "))

area_triangulo = (base_triangulo * altura_triangulo)/2

print (
    "A área do triangulo é: ",
    area_triangulo
)