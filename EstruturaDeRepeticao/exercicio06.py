'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''

contador = 0

while contador < 20:
    contador += 1
    print(contador)

contador2 = 0
while contador2 < 20:
    contador2 += 1
    print(contador2, end=' ')
