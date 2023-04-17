# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('---- ESCOLA PYTHON BRASIL ----')
print('Digite suas 4 notas para saber sua média: ')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A sua média foi de {media:.2f}')