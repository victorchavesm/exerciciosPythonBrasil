# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

print('---- ESCOLA PYTHON BRASIL ----')
print('Digite suas 3 notas para saber sua média: ')

nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
media = (nota1 + nota2 + nota3) / 3

if media > 10:
    print('Você digitou alguma nota errada pois sua média ficou maior que 10.')
elif media == 10:
    print(f'Aprovado com Distinção. \nSua média foi {media}')
elif media >= 7:
    print(f'Aprovado. \nSua média foi {media:.2f}')
else:
    print(f'Reprovado. \nSua média foi {media:.2f}')