# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
# depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais: 
# o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais:
# o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print('Valor mínimo para saque: R$ 10 \nValor máximo para saque: R$ 600 \nSomente valores inteiros.')
saque = int(input('Digite o valor para sacar: R$ '))

if saque < 10 or saque > 600:
    print(('Valor inválido.'))
else:
    nota100 = (saque // 100)
    saque = (saque - (nota100 * 100))
    print(f'{nota100} notas de R$ 100')

    nota50 = (saque // 50)
    saque = (saque - (nota50 * 50))
    print(f'{nota50} notas de R$ 50')

    nota10 = (saque // 10)
    saque = (saque - (nota10 * 10))
    print(f'{nota10} notas de R$ 10')

    nota5 = (saque // 5)
    saque = (saque - (nota5 * 5))
    print(f'{nota5} notas de R$ 5')

    nota1 = (saque // 1)
    saque = (saque - (nota1 * 1))
    print(f'{nota1} notas de R$ 1')
