# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite "F" para sexo Feminino ou "M" para Masculino: ').upper()

if sexo == 'F':
    print('Você selecionou Feminino.')
elif sexo == 'M':
    print('Você selecionou Masculino.')
else:
    print('Você não digitou F ou M.')
    