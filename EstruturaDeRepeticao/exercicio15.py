'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.
'''

n = int(input("Digite o número de termos da série de Fibonacci: "))

if n < 2:
    print("A série de Fibonacci requer pelo menos 2 termos.")
else:
    serie = [1, 1]

    while len(serie) < n:
        proximo_termo = serie[-1] + serie[-2]
        serie.append(proximo_termo)
        print(serie)

    print(f"Série de Fibonacci até o {n}-ésimo termo: {serie}")
