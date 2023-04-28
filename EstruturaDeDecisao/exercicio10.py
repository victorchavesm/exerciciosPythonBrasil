# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Informe qual turno você estuda. Digite M para Matutino, V para Vespertino ou N para Noturno: ').upper()

if turno == 'M':
    print('Você selecionou Matutino. \nBom dia!')
elif turno == 'V':
    print('Você selecionou Vespertino. \nBoa tarde!')
elif turno == 'N':
    print('Você selecionou Noturno. \nBoa noite!')
else:
    print('Valor inválido.')
    