# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
# (72.7*altura) - 58

altura = float(input('Digite sua altura (em metros): '))
pesoI = (72.7 * altura) - 58

print(f'De acordo com a fórmula (72.7*altura) - 58 = peso ideal, seu peso ideal é: {pesoI:.2f}')