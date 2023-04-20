# Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
# a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = int(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade da sua internet em Mbps: '))
tempo_download = tamanho / (velocidade/8) / 60

print(f'O tempo aproximado para o download ser concluído é: {tempo_download:.0f} minutos')