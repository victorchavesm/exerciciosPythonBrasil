# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
# lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# * salários até R$ 280,00 (incluindo) : aumento de 20%
# * salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# * salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# * salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# * o salário antes do reajuste;
# * o percentual de aumento aplicado;
# * o valor do aumento;
# * o novo salário, após o aumento.
print('-'*33)
print('PROGRAMA DE REAJUSTE DE SALÁRIOS')
print('-'*33)

salario = float(input('Informe seu salário ataual: R$ '))
print()
print('~ ~ ~ ~ ~ CALCULANDO ~ ~ ~ ~ ~')
print()
if salario <= 280:
    porcento = 20
elif salario <= 700:
    porcento = 15
elif salario < 1500:
    porcento = 10
else:
    porcento = 5

aumento = salario * (porcento/100)
salario_final = aumento + salario

print(f'O seu salário antes do aumento era: R$ {salario:.2f}')
print(f'Você recebeu {porcento}% de aumento.')
print(f'O aumento em reais foi o equivalente a: R$ {aumento:.2f}')
print(f'Seu salário após o aumento ficou: R$ {salario_final:.2f}')
