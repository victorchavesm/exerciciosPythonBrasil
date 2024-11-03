'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

litros = float(input('Digite o número de litros vendidos: '))
combustivel = input(
    'Digite o tipo de combustível [A - Álcool, G - Gasolina]: ')
preco_alcool = 1.9
preco_gasolina = 2.5

if combustivel.upper() == 'A':
    if litros <= 20:
        valor = litros * preco_alcool * 0.97
    else:
        valor = litros * preco_alcool * 0.95
elif combustivel.upper() == 'G':
    if litros <= 20:
        valor = litros * preco_gasolina * 0.96
    else:
        valor = litros * preco_gasolina * 0.94
else:
    print('Combustível inválido')

print(f'O valor a ser pago pelo cliente é: R$ {valor:.2f}')
