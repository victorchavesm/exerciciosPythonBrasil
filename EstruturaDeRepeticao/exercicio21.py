'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

'''
num = int(input('Digite um número inteiro: '))
if num < 2:
    print(f"{num} não é um número primo.")
else:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")

'''
Para curiosidade:
# Crivo de Eratóstenes:
# Solicitar ao usuário um número inteiro
n = int(input("Digite um número inteiro para encontrar todos os números primos até esse valor: "))

# Inicializar uma lista de booleanos representando se cada número é primo
# Inicialmente, assumimos que todos os números são primos (True)
primos = [True] * (n + 1)
primos[0] = primos[1] = False  # 0 e 1 não são primos

# Implementar o Crivo de Eratóstenes
p = 2
while p * p <= n:
    if primos[p]:
        for i in range(p * p, n + 1, p):
            primos[i] = False
    p += 1

# Coletar e imprimir todos os números primos
numeros_primos = [i for i, primo in enumerate(primos) if primo]
print(f"Números primos até {n}: {numeros_primos}")
'''
'''
# Crivo de Atkin

# Solicitar ao usuário um número inteiro
import math
n = int(input(
    "Digite um número inteiro para encontrar todos os números primos até esse valor: "))

# Inicializar uma lista de booleanos representando se cada número é primo
primos = [False] * (n + 1)

# Implementar o Crivo de Atkin
limite = int(math.sqrt(n)) + 1
for x in range(1, limite):
    for y in range(1, limite):
        # Primeiro conjunto de condições
        num = 4 * x**2 + y**2
        if num <= n and (num % 12 == 1 or num % 12 == 5):
            primos[num] = not primos[num]

        # Segundo conjunto de condições
        num = 3 * x**2 + y**2
        if num <= n and num % 12 == 7:
            primos[num] = not primos[num]

        # Terceiro conjunto de condições
        num = 3 * x**2 - y**2
        if x > y and num <= n and num % 12 == 11:
            primos[num] = not primos[num]

# Eliminar múltiplos de quadrados de números primos
for i in range(5, limite):
    if primos[i]:
        for j in range(i**2, n + 1, i**2):
            primos[j] = False

# 2 e 3 são primos
if n > 2:
    primos[2] = True
if n > 3:
    primos[3] = True

# Coletar e imprimir todos os números primos
numeros_primos = [i for i, primo in enumerate(primos) if primo]
print(f"Números primos até {n}: {numeros_primos}")
'''
