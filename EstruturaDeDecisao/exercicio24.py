'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input(
    'Digite a operação que deseja realizar: \n[+] \n[-] \n[*] \n[/] \n')

if operacao == '+':
    resultado = num1 + num2
    print(f'O resultado da operação é: {resultado}')
elif operacao == '-':
    resultado = num1 - num2
    print(f'O resultado da operação é: {resultado}')
elif operacao == '*':
    resultado = num1 * num2
    print(f'O resultado da operação é: {resultado}')
elif operacao == '/':
    resultado = num1 / num2
    print(f'O resultado da operação é: {resultado}')
else:
    print('Operação inválida')

if resultado % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

if resultado > 0:
    print('O número é positivo')
else:
    print('O número é negativo')

if resultado == int(resultado):
    print('O número é inteiro')
else:
    print('O número é decimal')
