'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
morango = float(input('Digite a quantidade de morangos em Kg: '))
maca = float(input('Digite a quantidade de maçãs em Kg: '))
preco_morango = 2.5
preco_maca = 1.8
if morango <= 5:
    valor_morango = morango * preco_morango
else:
    valor_morango = morango * 2.2
if maca <= 5:
    valor_maca = maca * preco_maca
else:
    valor_maca = maca * 1.5
valor_total = valor_morango + valor_maca
if morango + maca > 8 or valor_total > 25:
    valor_total *= 0.9
print(f'O valor a ser pago pelo cliente é: R$ {valor_total:.2f}')
