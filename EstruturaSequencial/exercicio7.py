# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o comprimento do lado do quadrado: '))
area = lado**2
dobro = area*2
print(f'A área do quadrado é: {area:.2f}')
print(f'O dobro da área é: {dobro}')
