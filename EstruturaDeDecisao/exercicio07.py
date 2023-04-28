# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite o último número inteiro: '))

if num1 == num2 and num2 == num3:
    print('Você digitou números iguais.')

else:
    if num1 > num2 and num1 > num3:
        print(f'O maior numero é: {num1}')
    elif num2 > num3:
        print (f'O maior numero é: {num2}')
    else:
        print (f'O maior numero é: {num3}')

    if num1 < num2 and num1 < num3:
        print(f'O menor numero é: {num1}')
    elif num2 < num3:
        print(f'O menor numero é: {num2}')
    else:
        print(f'O menor numero é: {num3}')
        