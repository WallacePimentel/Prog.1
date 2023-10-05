#Primeiro pedimos a entrada de uma frase e uma chave de espelhamento
frase = input().lower()

chave = input().lower()
if chave == "":
    chave = "abcdefghijklmnopqrstuvwxyz"

#Aqui definimos o comprimentos da chave e da frase, e o contador de deus respectivos índices e definindo uma frase final vazia
comprimento_chave = len(chave)
comprimento_frase = len(frase)
inicio_chave = 0
inicio_frase = 0
frase_final = ""

#Aqui estamos comparando o comprimento da chave e o index inicial dela e criamos uma dupla de espelhamento da chave que nos foi dada
while inicio_chave < comprimento_chave:
    dupla1,dupla2 = chave[inicio_chave] + chave[comprimento_chave-1]
    #Com essa dupla, pegamos a frase e passamos por cada índice dela e comparando se o caracter é igual a uma das letra da dupla,
    # se for igual trocamos pelo outro, se não for, adicionamos o caracter
    while inicio_frase < comprimento_frase:
        if frase[inicio_frase] == dupla1:
            frase_final += dupla2
        elif frase[inicio_frase] == dupla2:
            frase_final += dupla1
        else:
            frase_final += frase[inicio_frase]
        inicio_frase += 1
    #Aqui adicionamos os valores para fazer com que a busca siga para os próximos índices para formar uma nova dupla de espelhamento
    inicio_chave += 1
    comprimento_chave -= 1
    inicio_frase = 0
    
    #Aqui armazenamos a frase modificada pela primeira dupla e limpamos a variável que é utilizada para modificar as letra para reiniciar o
    # processo utilizando a frase modificada como base
    frase = frase_final
    frase_final = ""

print(frase)