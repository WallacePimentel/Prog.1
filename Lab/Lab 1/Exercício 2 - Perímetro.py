import math

#Import math foi utilizado para importar a biblioteca math

#Aqui estamos solicitando o raio do usuário
raio = float(input("Digite o valor do raio de sua circunferência em centímetros: "))

#Aqui calculamos o perímetro por 2 * pi * raio
perimetro = float(2 * math.pi * raio)

print("O perímetro da circunferência de raio", raio, "é", perimetro, "cm.")

