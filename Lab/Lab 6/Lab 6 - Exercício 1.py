#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

#Cria-se uma lista para armazenar os valores das cores das meias
meias = input().split()

#Uma lista para armazenar as meias ja contadas e uma para os valores dos pares
lista = []
soma = []

#Variável para somar os pares
final = 0

#Criamos um loop para comparar os valores de todas as meias e ver quantas iguais existem baseando-se na lista das que ja foram contadas
#Depois armazenamos na lista "soma" e somamos todos os valores dessa lista
for i in range(len(meias)): 
    if meias[i] not in lista:
        c = meias.count(meias[i])
        p = c // 2
        lista.append(meias[i])
        soma.append(p)
for x in range(len(soma)):
    final += soma[x]
print(final)