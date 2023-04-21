# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')
vogal = 'aeiou'
vogal2 = 'AEIOU'

if letra in vogal or letra in vogal2:
    print('A letra que você digitou é vogal')
else:
    print('A letra que você digitou é consoante.')