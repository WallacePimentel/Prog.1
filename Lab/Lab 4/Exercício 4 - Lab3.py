#Primeiro, exigimos o número que o usuário deseja obter a tabela
n = int(input("Entre com o número final da tabela de multiplicação:"))

#Aqui criamos uma estrutura de repetição para que o programa pudesse fornecer a tabela dos números de 1 x 1 até N x N
for x in range(1,n+1):
    for y in range(1,n+1):
        produto = x*y
        print(x,"x",y,"=",produto)
