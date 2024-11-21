'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

'''


def obter_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def calcular_anos(populacao_A, populacao_B, crescimento_A, crescimento_B):
    anos = 0
    while populacao_A < populacao_B:
        populacao_A += populacao_A * crescimento_A
        populacao_B += populacao_B * crescimento_B
        anos += 1
    return anos


while True:
    populacao_A = obter_valor_positivo(
        "Digite a população inicial do país A: ")
    populacao_B = obter_valor_positivo(
        "Digite a população inicial do país B: ")

    if populacao_A >= populacao_B:
        print("A população do país A já é maior ou igual à do país B.")
        continue

    crescimento_A = obter_valor_positivo(
        "Digite a taxa de crescimento anual do país A (em %): ") / 100
    crescimento_B = obter_valor_positivo(
        "Digite a taxa de crescimento anual do país B (em %): ") / 100

    anos = calcular_anos(populacao_A, populacao_B,
                         crescimento_A, crescimento_B)
    print(f"Será necessário {
          anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")

    repetir = input("Deseja realizar outra operação? (s/n): ").lower()
    if repetir != 's':
        print("Programa encerrado.")
        break
