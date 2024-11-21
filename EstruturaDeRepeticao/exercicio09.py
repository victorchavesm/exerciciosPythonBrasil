'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
# numeros = 0
# while numeros < 50:
#     numeros += 1
#     # print(numeros)
#     if numeros % 2 != 0:
#         numero_impar = numeros
#         print(numero_impar)


for numero in range(1, 51):
    if numero % 2 != 0:
        print(numero)
