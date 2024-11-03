def verificar_numero():
    numero = input("Digite um número: ")

    try:
        numero_float = float(numero)
        if numero_float == int(numero_float):
            print("O número é inteiro.")
        else:
            print("O número é decimal.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")


if __name__ == "__main__":
    verificar_numero()
