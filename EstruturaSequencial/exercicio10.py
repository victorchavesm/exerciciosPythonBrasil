# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (°C × 9/5) + 32

cel = float(input('Digite uma temperatura em Celsius (somente números): '))
fah = (cel * 9/5) + 32
print(f'{cel:.1f}°C é igual a: {fah:.1f}°F')