'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''

base = int(input('Digite a base: '))
expo = int(input('Digite o expoente: '))
resultado = 1
for i in range(expo):
    resultado *= base
print(f"{base} elevado a {expo} é {resultado}")
