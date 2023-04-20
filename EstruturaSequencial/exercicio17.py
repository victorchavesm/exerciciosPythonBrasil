# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input('Digite a área total em m² a ser pintada: '))

quantidade_litros = (area / 6) * 1.1 # + 10%
latas = int(quantidade_litros / 18)
galoes = int(quantidade_litros / 3.6)

# Latas:
if quantidade_litros % 18 != 0:
    latas += 1
precoL = latas * 80

# Galões:
if quantidade_litros % 18 != 0:
    galoes += 1
precoG = galoes * 25

# Latas + Galões:
misturaL = int(quantidade_litros / 18.0)
misturaG = int((quantidade_litros - (misturaL * 18)) / 3.6)

if ((quantidade_litros - (misturaL * 18) % 3.6 != 0)):
    misturaG += 1
precoM = (misturaL * 80) + (misturaG * 25)

# -----------
print('-'*50)
print(f'Apenas latas de 18 litros: \nSeriam necessárias {latas} latas, o que daria: R$ {precoL:.2f}')
print('-'*50)
print(f'Apenas galões de 3.6 litros: \nSeriam necessários {galoes} galões, o que daria: R$ {precoG:.2f}')
print('-'*50)
print(f'Misturando latas e galões:\nSeriam necessárias {latas} latas e {galoes} galões, o que daria: R$ {precoM:.2f}')


