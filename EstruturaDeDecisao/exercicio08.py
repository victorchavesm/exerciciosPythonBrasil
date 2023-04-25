# Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input('Informe o preço do primeiro produto: R$ '))
prod2 = float(input('Informe o preço do segundo produto: R$ '))
prod3 = float(input('Informe o preço do terceiro produto: R$ '))

if prod1 == prod2 and prod1 == prod3:
    print('Os preços são iguais, compre qualquer um.')

if prod1 < prod2 and prod1 < prod3:
    menor  = prod1
elif prod2 < prod1 and prod2 < prod3:
    menor = prod2
else:
    menor = prod3
print(f'Você deve comprar o produto que custa R$ {menor:.2f}')

