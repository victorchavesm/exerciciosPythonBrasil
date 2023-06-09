# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são 
# do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato 
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valor_hora = float(input('O valor da sua hora trabalhada é: R$ '))
quantidade_horas = int(input('Quantas horas você trabalhou esse mês? '))
salario_bruto = valor_hora * quantidade_horas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 5
elif salario_bruto <= 2500:
    ir = 10
else:
    ir = 20

desconto_IR = (salario_bruto * ir) /100
inss = (salario_bruto * 10) / 100
sindicato = (salario_bruto * 3) / 100
total_descontos = desconto_IR + inss + sindicato
fgts = (salario_bruto * 11 ) / 100 # não é pra descontar
salario_liquido = salario_bruto - total_descontos

print(f'    Salário bruto:              R$ {salario_bruto:.2f}')
print(f'    FGTS (11%) :                R$ {fgts:.2f} (depositado pela empresa)')
print(f'(-) IR ({ir}%):                 R$ {desconto_IR:.2f}')
print(f'(-) INSS (10%):                 R$ {inss:.2f}'),
print(f'(-) Sindicato (3%)              R$ {sindicato:.2f}')
print(f'    Total de descontos:         R$ {total_descontos:.2f}')
print(f'    Salário líquido:            R$ {salario_liquido:.2f}')

