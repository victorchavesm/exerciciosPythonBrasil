'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
'''
n = int(input("Digite o número de termos da série de Fibonacci: "))

if n < 2:
    print("A série de Fibonacci requer pelo menos 2 termos.")
else:
    serie = [1, 1]

    while len(serie) < n:
        proximo_termo = serie[-1] + serie[-2]
        if proximo_termo > 500:
            break
        serie.append(proximo_termo)
        print(serie)

    print(f"Série de Fibonacci até que o valor seja maior que 500: {serie}")
