#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

#Primeiro criamos uma lista dos valores e criamos um loop para transformar essa lista de strings em uma lista de inteiros
valores1 = input().split()
valores = []
for i in range(len(valores1)):
    valores.append(int(valores1[i]))

#Criamos um valor de comparação "maior" para armazenar o maior lucro
maior = -1

#Aqui foi feito um loop para fazer a diferença do valor no dia de compra e no dia de venda
for h in range(len(valores)):
    for x in range(len(valores)):

        #Esta estrutura de decisão serve para somente fazer a operação quando o dia de venda for depois do dia de compra
        if i > h:
            op = valores[i] - valores[h]
            if op > maior:
                print(op)
                maior = op
print(f"O lucro máximo é {maior}")