'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''

while True:
    nota = input('Digite um número entre 0 e 10: ')
    try:
        nota_float = float(nota)
        if 0 <= nota_float <= 10:
            print(f'Você digitou uma nota válida: {nota_float}')
            break
        else:
            print('Valor inválido, digite novamente um valor entre 0 e 10')
    except ValueError:
        print('Digite um número válido entre 0 e 10')
