#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

#Definindo a função
def maior(arquivo):
    #Abrindo o arquivo
    arq = open(arquivo)
    #Sentinela da maior palavra
    m = ""
    #Leia as linhas do arquivo e passe uma por uma através de um loop
    palavras = arq.readlines()
    for i in palavras:
        #Divida as palavras da linha
        linha = i.split()
        for h in linha:
            #Passe por cada palavra e remova o "\n" se ele existir na palavra
            h = h.strip("\n")
            #Comparando se a palavra é maior que a maior palavra atual
            if len(h) > len(m):
                m = h
    #Fechando o arquivo e retornando a maior palavra
    arq.close()
    return m

#Solicitando o nome e o diretório dele se necessário e executando a função
arquivo_usuario = input("Entre com o arquivo: ")
print(maior(arquivo_usuario))