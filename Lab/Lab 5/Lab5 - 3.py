#Aqui estamos solicitando os elementos da lista e a posição do elemento a ser retirado
lista = input("Entre com os elementos da lista:").split()
posição_retirada= int(input("Entre com a posição do elemento a ser retirado:"))
#Aqui criamos duas listas vazias para usa-las depois
lista1 = []
lista2 = []

#Aqui estamos somando a lista1 os elementos vão do elemento da posição 0 até o elemento
#nterior a posição a ser retirada
for i in range(posição_retirada):
    lista1.append(lista[i])
#Aqui estamos somando a lista2 os elementos que vão do elemento posterior a ser retirado
#até ao final da lista
for x in range(posição_retirada + 1, len(lista) ):
    lista2.append(lista[x])
#Aqui estamos imprimindo a lista1 + lista2 que exclui o elemento a ser retirado.
print(lista1 + lista2)