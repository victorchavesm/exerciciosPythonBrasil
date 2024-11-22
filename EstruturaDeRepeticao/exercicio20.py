'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

while True:
    numero = int(input('Digite um número inteiro positivo menor que 16: '))
    fatorial = 1
    if numero == 0:
        print("Programa encerrado.")
        break
    elif numero < 0 or numero >= 16:
        print("Número inválido. Por favor, digite um número positivo menor que 16.")
        continue
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"{numero}! = {fatorial}")
