# '''
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# '''

# while True:
#     nome = input('Digite um nome: ')
#     idade = input('Digite a idade: ')
#     salario = input('Digite o salário: ')
#     sexo = input('Digite o sexo: \n[F] Feminino \n[M] Masculino \n')
#     estado_civil = input(
#         'Digite o estado civil: \n[S] Solteiro \n[C] Casado \n[V] Viúvo \n[D] Divorciado \n')
#     try:
#         idade_int = int(idade)
#         salario_float = float(salario)
#         sexo_lower = sexo.lower()
#         estado_civil_lower = estado_civil.lower()

#         if len(nome) < 3:
#             print('Nome precisa ser maior que 3 caracteres.')
#         if idade_int < 0 or idade_int > 150:
#             print('Idade inválida. Tente novamente.')
#         if salario_float < 0:
#             print('Salário deve ser maior que zero.')
#         if sexo != 'm' and sexo != 'f':
#             print('Você digitou algo errado no gênero.')
#         if estado_civil != 's' and estado_civil and 'c' and estado_civil and 'v' and estado_civil != 'd':
#             print('Você digitou algo errado no estado civil.')
#     except ValueError:
#         print('Você digitou algum valor inválido.')
#     break

def validar_nome():
    while True:
        nome = input('Digite um nome: ')
        if len(nome) > 3:
            return nome
        else:
            print('Nome precisa ter mais de 3 caracteres.')


def validar_idade():
    while True:
        try:
            idade = int(input('Digite a idade: '))
            if 0 <= idade <= 150:
                return idade
            else:
                print('Idade inválida. Deve ser entre 0 e 150.')
        except ValueError:
            print('Você digitou um valor inválido para idade. Tente novamente.')


def validar_salario():
    while True:
        try:
            salario = float(input('Digite o salário: '))
            if salario > 0:
                return salario
            else:
                print('Salário deve ser maior que zero.')
        except ValueError:
            print('Você digitou um valor inválido para salário. Tente novamente.')


def validar_sexo():
    while True:
        sexo = input(
            'Digite o sexo: \n[F] Feminino \n[M] Masculino \n').lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print(
                'Você digitou algo errado no sexo. Tente "F" para feminino ou "M" para masculino.')


def validar_estado_civil():
    while True:
        estado_civil = input(
            'Digite o estado civil: \n[S] Solteiro \n[C] Casado \n[V] Viúvo \n[D] Divorciado \n').lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print('Você digitou algo errado no estado civil. Tente novamente.')


# Chamando cada função para coletar e validar os dados
nome = validar_nome()
idade = validar_idade()
salario = validar_salario()
sexo = validar_sexo()
estado_civil = validar_estado_civil()

# Exibindo as informações válidas
print(f'\nInformações Validadas:\nNome: {nome}\nIdade: {idade}\nSalário: {
      salario}\nSexo: {sexo.upper()}\nEstado Civil: {estado_civil.upper()}')
