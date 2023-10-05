#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

#Criando a função de conferir os assentos
def conf_assentos_juntos(lista,b):
    #Contador para as possíveis maneiras de se sentar
    contador = 0
    #Loop para passar por cada linha da matriz fornecida
    for i in lista:
        #Loop para ir de 0 até o tamanho da matriz menos a quantidade de assentos necessária, para não extrapolar na hora de utilizar os índices
        for x in range(len(i) -b+1):
            resultado = True
            #Loop para passarmos da cadeira que estamos até a quantidade de assentos necessários, verificando se eles estão vazios
            for z in range(b):
                #Se não estiverem vazios, resultado é falso
                if i[x] != 0 or i[z+x] !=0:
                    resultado = False
            #Se estiverem, o resultado continua true e adicionamos 1 ao contador de maneiras de se sentar       
            if resultado == True:
                contador +=1
    return contador

#Solicitando a função para a matriz
print(conf_assentos_juntos([[1, 0, 1, 0, 1, 0, 1],[0, 1, 0, 1, 0, 1, 0],[0, 0, 1, 1, 1, 1, 1],[1, 0, 1, 1, 0, 0, 1],[1, 1, 1, 0, 1, 0, 1],[0, 1, 1, 1, 1, 0, 0]],2))