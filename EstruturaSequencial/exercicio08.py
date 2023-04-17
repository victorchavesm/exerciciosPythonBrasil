# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

ganha_hora = float(input('Informe quanto você ganha por hora: R$'))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas no mês: '))
salario = ganha_hora * horas_trabalhadas

print(f'Seu salário esse mês foi: R${salario:.2f}')