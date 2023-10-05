#Aqui solicitamos a lista e o item a ser procurado
lista = input("Entre com os elementos da lista:").split()
procura = input()
indices = []

#Aqui verificamos se o elemento é igual a algum da lista e se for anotamos o índice dessa
#ocorrência na lista
for i in range(len(lista)):
    if lista[i] == procura:
        indices.append(i)

#Aqui verificamos se o elemento não está na lista
if procura not in lista:
    print("O elemento",procura,"está na posição -1")
else:
    print("O elemento",procura,"está na posição",indices[0])