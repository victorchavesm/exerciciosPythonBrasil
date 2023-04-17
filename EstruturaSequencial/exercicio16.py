# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# 1 litro = 3m²
# 18 litros = 54m²
# 1 lata = R$ 18.00

area = float(input('Digite a área total em m² a ser pintada: '))
quantidade_litros = area / 3
latas = int(quantidade_litros / 18)
preco = latas * 18

if quantidade_litros % 18 != 0:
    latas += 1

print(f'O total de latas necessárias para pintar esse local é: {latas}')
print (f'O preço total da compra será: {preco:.2f}')