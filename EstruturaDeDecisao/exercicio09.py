# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite um último número: '))

if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num1 and num2 > num3:
        meio = num2
        menor = num3
    else:
        menor = num2
        meio = num3
elif num2 > num1 and num2 > num3:
    maior = num2
    if num3 > num1:
        menor = num1
        meio = num3
    else:
        menor = num3
        meio = num1
else:
    maior = num3
    if num2 > num1:
        menor = num1
        meio = num2
    else:
        menor = num2
        meio = num1

print(f'A ordem decrescente dos números digitados é: {maior}, {meio}, {menor}')