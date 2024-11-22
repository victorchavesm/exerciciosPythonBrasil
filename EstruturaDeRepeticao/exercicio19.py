'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

lista = []
resposta = ''
maior = 0
menor = 0
soma = 0
while True:
    numero = int(input('Digite um número entre 0 e 1000: '))
    if numero < 0 or numero > 1000:
        print('Você digitou número fora do intervalo. Programa sendo encerrado.')
        break
    else:
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
