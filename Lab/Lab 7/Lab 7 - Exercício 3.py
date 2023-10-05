#Dupla: Wallace da Rocha Pimentel Júnior

#Primeiramente, criamos uma função para conseguir uma lista de divisores dada uma determinada variável
def div(x):
    #Criamos uma lista vazia, passamos por todos os números de 2 ao número escolhido e verificamos quais deles, quando dividindo o número, resulta no resto 0
    lista = []
    for i in range(2,x+1):
        if x%i == 0:
            #Se o resto resulta em 0, guardamos o número na lista de divisores
            lista.append(i)
    return lista

#Enfim, criamos a função para verificar se dado três números, eles formam uma tripla pitagórica primitiva
def pitagoras(x,y,z):
    #Primeiro definimos uma variável primit verdadeira e verificamos com 2 loops se o item de uma lista de divisores de um dos três números está presente nas outras
    #Se sim, definimos primit como false
    primit = True
    for i in div(x):
        if i in div(y) or i in div(z):
            primit = False
    for h in div(y):
        if h in div(z):
            primit = False
    
    #Se a tripla realmente for primitiva, criamos uma estrutura de repetição para avaliar qual o maior número e em seguida retornamos com a avaliação do teorema de pitágoras aplicado
    #sobre eles, se o resultado for correto, retornará como True
    if primit == True:
        if x > y and x > z:
            return ((y ** 2) + (z ** 2) == (x ** 2))
        elif y > z:
            return ((x ** 2) + (z ** 2) == (y ** 2))
        else:
            return ((x ** 2) + (y ** 2) == (z ** 2))
    
    else:
        return primit

#Aqui estamos solicitando as 3 variáveis, definindo-as como inteiros e ativando a função em seguida
x,y,z = input().split()
x = int(x)
y = int(y)
z = int(z)

print(pitagoras(x,y,z))