# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fah = float(input('Digite uma temperatura em Fahrenheit (somente números): '))
cel = 5 * ((fah - 32) / 9)
print(f'{fah:.1f}°F é igual a: {cel:.1f}°C')