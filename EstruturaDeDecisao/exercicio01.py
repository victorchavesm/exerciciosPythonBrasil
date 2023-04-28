# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print(f'O maior número é {num1}')
elif num1 < num2:
   print(f'O maior número é {num2}')
else:
    print('Os números são iguais')
    