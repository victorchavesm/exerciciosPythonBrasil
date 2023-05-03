# Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input('Digite um lado: '))
lado2 = float(input('Digite outro: '))
lado3 = float(input('Digite o último lado: '))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print('Não é um triangulo.')
else: 
    if (lado1 == lado2) and (lado1 == lado3) :
        triangulo = 'Equilátero'
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        triangulo = 'Isósceles'
    else:
        triangulo = 'Escaleno'
    print(f'É um triângulo do tipo {triangulo}')