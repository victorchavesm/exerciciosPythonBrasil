'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

menor = min(num1, num2)
maior = max(num1, num2)
soma = 0

for i in range(menor + 1, maior):

    print(f'{soma} + {i} =')
    soma += i
    print(soma)
