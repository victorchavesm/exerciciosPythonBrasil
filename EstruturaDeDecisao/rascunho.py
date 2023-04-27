salario = float(input("Digite o salário atual do colaborador: "))

if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento

print("Salário antes do reajuste: R$ {:.2f}".format(salario))
print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
print("Valor do aumento: R$ {:.2f}".format(valor_aumento))
print("Novo salário após o aumento: R$ {:.2f}".format(novo_salario))