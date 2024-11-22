'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

lista = []
resposta = ''
maior = 0
menor = 0
soma = 0
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)
    resposta = input(
        'Deseja continuar a adicionar números a lista? [S] / [N]')
    if resposta.lower() == 's':
        continue
    else:
        break
print(f'Lista: {lista} \nMenor: {menor} \nMaior: {maior} \nSoma: {soma}')
