#Função para criar o tabuleiro
def tabuleiro_xadrez(x, y, z):
    #Verificando se os elementos do tabuleiro são idênticos
    if y == z:
        return "Inválido"
    else:
        #Matriz do tabuleiro vazia
        lista = []
        #Variável de verificação se atingimos a quantidade de linhas requisitada e também se estamos em uma linha ímpar ou par
        v = 0
        #Loop enquanto não atingirmos a quantidade de linhas requisitada
        while v < int(x):
            #Se estamos numa linha par, criamos uma lista com "y,z" vezes a quantidade de linhas e adicionamos na matriz final
            if v % 2 == 0:
                listai = [y,z]*int(x)
                lista.append(listai[0:int(x)])
            #Se estamos numa linha ímpar, criamos uma lista com "y,z" vezes a quantidade de linhas e adicionamos na matriz final
            elif v % 2 != 0:
                listai = [z, y] * int(x)
                lista.append(listai[0:int(x)])
            #Adicionamos 1 á "v" para passar pra próxima linha
            v +=1
        return lista

#Solicitando as variáveis
x,y,z = input().split()

#Ativando a função para a matriz "lista" e escrevendo o tabuleiro utilizando um loop que passa por todos os itens de "lista", caso a matriz seja válida
lista = tabuleiro_xadrez(x,y,z)
if lista != "Inválido":
    for i in lista:
        print(i)
else:
    print(lista)