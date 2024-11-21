'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

lista = []

while len(lista) < 5:
    valor = int(input("Informe um número: "))
    lista.append(valor)

media = sum(lista) / len(lista)
print(media)
