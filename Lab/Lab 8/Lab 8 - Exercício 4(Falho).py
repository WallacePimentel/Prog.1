def organizador_de_nomes(arquivo_nomes):
    arq1 = open(arquivo_nomes)
    
    linhas = arq1.readlines()
    nomes = []
    for i in linhas:
        i = i.split()
        nome_atual = ""
        for h in range(0,len(i)-3):
            nome_atual += i[h]
            nome_atual += " "
        nomes.append(nome_atual)
    arq1.close()
    return nomes

def total_de_medalhas_e_ouro(arquivo_totais):
    arq = open(arquivo_totais)
    linhas = arq.readlines()
    totais = []
    for i in linhas:
        i = i.split()
        total = 0
        for h in range(1,4):
            total += int(i[-h])
        totais.append(total)
    arq.close()
    return totais

def olimpiada(arquivo1,arquivo2):
    nomes = organizador_de_nomes(arquivo1)
    totais = total_de_medalhas_e_ouro(arquivo1)
    arq = open(arquivo1)
    linhas = arq.readlines()
    ouro = []
    maior_ouro = 0
    resultado = []
    for i in linhas:
        i = i.split()
        ouro.append(int(i[-3]))
    for h in range(len(ouro)):
        if h < len(ouro) - 1:
            if ouro[h] > ouro[h+1]:
                temp = ouro[h]
                ouro[h] = ouro[h+1]
                ouro[h+1] = temp
                temp2 = nomes[h]
                nomes[h] = nomes[h+1]
                nomes[h+1] = temp2
                temp3 = totais[h]
                totais[h] = totais[h+1]
                totais[h+1] = temp3
    for z in range(len(nomes)):
        final = (f"{nomes[z]} , total = {totais[z]}")
        resultado.append(final)
    arq2 = open(arquivo2,"w")
    for b in resultado:
        arq2.write(b)
        arq2.write("\n")
    arq.close()
    arq2.close()
    return ouro

print(olimpiada("teste.txt","teste2.txt"))