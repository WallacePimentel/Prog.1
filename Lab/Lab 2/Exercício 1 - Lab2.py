#Aqui vamos recolher os valors de a, b, c e d
a = int(input("Entre com o valor de A: "))
b = int(input("Entre com o valor de B: "))
c = int(input("Entre com o valor de C: "))
d = int(input("Entre com o valor de D: "))

#Aqui vamos fazer todas as comparações necessárias para que os valores sejam aceitos
if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print("Valores Aceitos.")
else:
    print("Valores não aceitos.")