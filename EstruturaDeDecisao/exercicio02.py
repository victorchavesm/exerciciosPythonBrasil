# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input('Digite um número positivo ou negativo: '))

if valor < 0:
    print(f'{valor} é um número negativo.')
elif valor > 0:
     print(f'{valor} é um número positivo.')
else:
    print(f'Você digitou zero. \nZero é um número neutro, ou seja, não é um número nem positivo e nem negativo.')
    