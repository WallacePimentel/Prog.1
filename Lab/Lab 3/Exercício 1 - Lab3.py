# Aqui estamos exigindo um valor do número e definindo o contador como zero
n = int(input("Digite um número inteiro:"))
c = 0

#Aqui estamos criando um loop para que enquanto o número for maior que 1, divida ele por 10 e a cada vez que isso ocorre adicionar 1 no contador para achar a quantidade de dígitos
while n>1:
    n = n/10
    c = c+1
#Aqui estamos especificando uma exceção quando o número for 0, o quantidade de dígitos ser 1, pois dentro da divisão daria 0
if n == 0:
    c = 1
print("A quantidade de dígitos é igual:", c)
