#6. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Entre com o valor do raio do círculo: "))

#area = pi  *  r**2
area = 3.14 * raio**2

print(f'A área é {area:.2f}')