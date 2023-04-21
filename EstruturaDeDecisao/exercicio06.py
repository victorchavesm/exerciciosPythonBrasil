# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite o último número inteiro: '))

if num1 == num2 and num2 == num3:
    print('Você digitou números iguais.')
elif num1 > num2 and num1 > num3:
    print(f'{num1} é o maior número digitado.')
elif num2 > num3:
    print(f'{num2} é o maior número digitado.')
else:
    print(f'{num3} é o maior número digitado.')