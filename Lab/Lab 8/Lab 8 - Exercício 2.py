#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

#Definindo a função
def repete(arquivo):
    #Abrindo o arquivo
    arq = open(arquivo)
    #Lendo o arquivo
    linhas = arq.readlines()
    #Definindo uma sentinela para a palavra mais repetida e uma para a quantidade de vezes que foi repetida para comparar
    maior_repetido = 0
    palavra_repetida = ""
    #Passando por cada linha com um loop
    for h in linhas:
        #Divindo as palavras da linha
        palavras = h.split()
        for i in palavras:
            #Passe por cada palavra e remova o "\n" se ele existir na palavra
            i = i.strip("\n")
            #Se a quantidade de vezes que a palavra atual aparece em palavras for maior que a maior atual, subistitua ela pela atual e guarde sua quantidade de repetições
            if palavras.count(i) >= maior_repetido:
                maior_repetido = palavras.count(i)
                palavra_repetida = i
    #Feche o arquivo e retorne a palavra mais repetida
    arq.close()
    return palavra_repetida

#Solicitando o arquivo e executando a função
arquivo_usuario = input("Entre com o arquivo: ")
print(repete(arquivo_usuario))
