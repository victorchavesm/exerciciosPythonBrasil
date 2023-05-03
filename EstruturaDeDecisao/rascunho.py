lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if (lado1 > (lado2 + lado3)) or (lado2 > (lado1 + lado3))\
        or (lado3 > (lado1 + lado2)):
    ehTriangulo = False
else:
    ehTriangulo = True

if (ehTriangulo):
    print ('Os valores formam um Triangulo')
 
else:
    print ('Os valores nao formam um Triangulo')