# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input('Informe um número inteiro entre 1 e 7: '))

if num == 1:
    dia = 'Domingo'
elif num == 2:
    dia = 'Segunda-feira'
elif num == 3:
    dia = 'Terça-feira'
elif num == 4:
    dia = 'Quarta-feira'
elif num == 5:
    dia = 'Quinta-feira'
elif num == 6:
    dia = 'Sexta-feira'
elif num == 7:
    dia = 'Sábado'
else:
   dia = 'um valor inválido.'
print(f'O número que você digitou equivale a {dia}')