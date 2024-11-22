'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

(esse aqui foi IA que fez)
'''
# Solicitar ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é primo
if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    eh_primo = True
    divisores = []
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            divisores.append(i)
            if i != numero // i:  # Adicionar o par divisor se não for o mesmo
                divisores.append(numero // i)

    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        divisores.sort()
        print(f"{numero} não é um número primo. Ele é divisível por: {divisores}")
