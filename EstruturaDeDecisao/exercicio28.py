'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''
tipo_carne = input(
    'Digite o tipo de carne [F - Filé Duplo, A - Alcatra, P - Picanha]: ')
quantidade = float(input('Digite a quantidade de carne em Kg: '))
preco_filé_duplo = 4.9
preco_alcatra = 5.9
preco_picanha = 6.9
if tipo_carne.upper() == 'F':
    if quantidade <= 5:
        valor = quantidade * preco_filé_duplo
    else:
        valor = quantidade * 5.8
elif tipo_carne.upper() == 'A':
    if quantidade <= 5:
        valor = quantidade * preco_alcatra
    else:
        valor = quantidade * 6.8
elif tipo_carne.upper() == 'P':
    if quantidade <= 5:
        valor = quantidade * preco_picanha
    else:
        valor = quantidade * 7.8
else:
    print('Tipo de carne inválido')
pagamento = input(
    'Digite o tipo de pagamento [C - Cartão Tabajara, D - Dinheiro]: ')
if pagamento.upper() == 'C':
    valor *= 0.95
print('-'*20)
print(f'CUPOM FISCAL\n')
print(f'Tipo de carne: {tipo_carne}')
print(f'Quantidade: {quantidade} Kg')
print(f'Preço total: R$ {valor:.2f}')
print(f'Tipo de pagamento: {pagamento}')
if pagamento.upper() == 'C':
    print(f'Valor do desconto: R$ {quantidade * valor * 0.05:.2f}')
print(f'Valor a pagar: R$ {valor:.2f}')
print('-'*20)
