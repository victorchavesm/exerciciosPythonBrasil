# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input('Informe seu sexo F/M: ')
altura = float(input('Digite sua altura (em metros): '))

if sexo == 'M':
    pesoI = (72.7 * altura) - 58
else:
    pesoI = (62.1 * altura) - 44.7

print(f'Seu peso ideal é: {pesoI:.2f}')