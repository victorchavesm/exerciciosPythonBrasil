# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Informe uma data no formato dd/mm/aaaa: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

if ano < 0:
    print('Ano inválido.')
if dia < 0 or dia > 31:
    print('Dia inválido.')
if mes < 1 or mes > 12:
    print('Mês inválido.')
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia > 0 and dia < 32:
            print('Data válida.')
        else:
            print('Dia inválido.')
    elif mes in [4, 6, 9, 11]:
        if dia > 0 and dia < 31:
            print('Data válida.')
        else:
            print('Dia inválido.')
    else: #fevereiro
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia > 0 and dia < 30:
                print('Data válida.')
            else:
                print('Dia inválido')
        else:
            if dia > 0 and dia < 29:
                print('Data válida.')
            else:
                print('Dia inválido.')