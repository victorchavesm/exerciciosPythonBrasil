'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''

entrada = 0
lista_par = []
lista_impar = []
while entrada < 10:
    entrada += 1
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 < 1:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print(f'Você digitou {len(lista_par)} números pares: {lista_par}')
print(f'Você digitou {len(lista_impar)} números ímpares: {lista_impar}')
