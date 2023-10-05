#Aqui estamos coletando o número
n = int(input("Entre com um número de 5 dígitos: "))

#Aqui estamos coletando cada algarismo do número, divindo o número inteiro pela base 10 do algarismo que queremos encontrar
d1 = n // 10000
r1 = n - (d1 * 10000)
d2 = r1 // 1000
r2 = r1 - (d2 * 1000)
d3 = r2 // 100
r3 = r2 - (d3 * 100)
d4 = r3 // 10
r4 = r3 - (d4 * 10)
d5 = r4

#Aqui estamos comparando se os digitos se igualam para ser um palíndromo
if d1==d5 and d2==d4:
    print("O número é um palíndromo")
else:
    print("O número não é um palíndromo")