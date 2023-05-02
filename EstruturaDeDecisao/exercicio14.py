# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e 
# a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

print('---- ESCOLA PYTHON BRASIL ----')
print('Digite suas 2 notas para saber sua média: ')

nota1 = float(input('Nota 1ª unidade: '))
nota2 = float(input('Nota 2ª unidade: '))
media = (nota1 + nota2) / 2

if media > 10:
    print('Erro: Você digitou algum valor errado pois sua média excedeu o limite 10.')
else:
    if media >= 9:
        conceito = 'A'
    elif media >= 7.5:
        conceito = 'B'
    elif media >= 6:
        conceito = 'C'
    elif media >= 4:
        conceito = 'D'
    else:
        conceito = 'E'
    print(f'A sua média foi {media:.1f}') 
    print(f'Conceito {conceito}')

    if conceito in 'ABC':
        print('APROVADO')
    else:
        print('REPROVADO')