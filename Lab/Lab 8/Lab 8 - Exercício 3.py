#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

#Definindo a função
def letras_agrupadas(arquivo,n):
    #Abrindo o arquivo
    arq = open(arquivo, "w")
    #Criando uma lista com o alfabeto e uma lista vazia para as divisões
    alfa = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list = []
    #Loop para passar pelas primeiras letras de cada linha
    for i in range(0,26,n):
        #Criando uma string vazia para concatenarmos as letras da linha
        r = ""
        #Loop para passar pela primeira letra da linha e pelas n letras seguintes, de acordo com o número dado pelo usuário
        for h in range(n):
            #Se o índice da letra estiver contido no alfabeto continuar, para evitar extrapolação
            if i+h < 26:
                #Adicionar as letras da linha na string
                r += alfa[i+h]
        #Apendar a string da linha na lista        
        list.append(r)
    #Passar por cada linha da lista e escreve-la no arquivo, pulando a linha entre cada uma    
    for z in list:
        arq.write(z)
        arq.write("\n")
    #Fechando o arquivo
    arq.close()

#Solicitando o arquivo, o número para as divisões e executando a função
arquivo_usuario = input("Entre com o arquivo: ")
num = int(input("Entre com o número de divisão: "))
letras_agrupadas(arquivo_usuario,num)