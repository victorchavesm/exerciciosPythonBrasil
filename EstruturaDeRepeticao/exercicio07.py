'''
Faça um programa que leia 5 números e informe o maior número.
'''

lista = []

while len(lista) < 5:
    valor = int(input("Informe um número: "))
    lista.append(valor)

print(max(lista))
