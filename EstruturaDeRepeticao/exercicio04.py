'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

populacao_A = 80000
populacao_B = 200000
crescimento_A = 3/100
crescimento_B = 1.5/100
anos = 0
while populacao_A < populacao_B:
    populacao_A = populacao_A + (populacao_A * crescimento_A)
    populacao_B = populacao_B + (populacao_B * crescimento_B)
    anos += 1
print(f'Será necessário {
      anos} anos para a população da cidade A ultrapassar a população da cidade B.')
