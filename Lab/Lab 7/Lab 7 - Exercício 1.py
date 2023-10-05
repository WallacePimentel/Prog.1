#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

#Primeiramente, criamos uma função para encontrar o fatorial de um número
def fatorial(x):
    resultado = 1
    #Loop de 1 ao número, multiplicando a variável "resultado" pelos números até o número fornecido
    for i in range(1,x+1):
        resultado = resultado*i
    return resultado

#Função de kempner
def kempner(y):
    #Variável criado para verificar qual fatorial divido pelo número fornecido resulta em resto 0
    c = 1
    #Se a operação citada anteriormente resultar 0, retornamos o número, se não, adicionamos 1 a váriavel "c" até encontrar o número
    while fatorial(c)% y != 0:
        c += 1
    return c

#Solicite o número inteiro
num = int(input("Entre com o número: "))

#Escreva o resultado de kempner
print(f"kempner({num}) --> {kempner(num)}")