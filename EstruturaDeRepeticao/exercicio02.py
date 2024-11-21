'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    user = input('Digite um nome de usuário: ')
    password = input('Digite uma senha: ')
    try:
        if user == password:
            print('Usuário e senha não podem ser iguais.')
            continue
        if user == ' ' or user == '' or password == ' ' or password == '':
            print('Os campos não podem ficar vazios.')
            continue
    except ValueError:
        print('Você digitou algum valor inválido.')
    break
