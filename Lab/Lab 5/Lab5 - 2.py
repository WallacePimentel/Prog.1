#Aqui estamos solicitando os elementos da lista, o elemento a ser elemento inserido
#e a posição a inserir o elemento
lista = input("Entre com os elementos da lista:").split()
elemento_inserido = input("Entre com o elemento a ser inserido:")
posicao = int(input("Entre com a posição para inserir o elemento:"))

#Aqui iniciamos uma lista vazia e somamos a ela os elementos da posição 0 até a 
#posição a qual o elemento vai ser inserido
primeira_parte = []
for i in range(posicao):
    primeira_parte.append(lista[i])

#Aqui iniciamos uma lista vazia e somamos a ela os elementos da posição a qual o 
#elemento vai ser inserido até o final da lista
segunda_parte = []
for x in range(posicao, len(lista)):
    segunda_parte.append(lista[x])
lista_elemento = [elemento_inserido]
lista_final = primeira_parte + lista_elemento + segunda_parte
print(lista_final)