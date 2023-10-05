import math

#Aqui estamos coletando as coordenadas
x1 = float(input("Entre com a coordenada x do ponto a: "))
y1 = float(input("Entre com a coordenada y do ponto a: "))
x2 = float(input("Entre com a coordenada x do ponto b: "))
y2 = float(input("Entre com a coordenada y do ponto b: "))
x3 = float(input("Entre com a coordenada x do ponto c: "))
y3 = float(input("Entre com a coordenada y do ponto c: "))

#Aqui estamos calculando a distância entre as coordenadas utilizando o teorema de pitágoras
d12 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
d23 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
d31 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

#Aqui estamos comparando para ver se as coordenadas fornecidas geram um triângulo
#Em seguida comparando seus lados para ver o seu tipo
if (d12 + d23) > d31 and (d23 + d31) > d12 and (d12 + d31) > d23:
    if d12==d23==d31:
        print("É um triângulo equilátero")
    elif d12==d23 or d23==d31 or d12==d31:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("As coordenadas não geram um triângulo.")