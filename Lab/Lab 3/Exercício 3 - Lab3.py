c = 0
total = 0
#Primeiro definimos o contador de números positivos e o total da soma dos números inseridos

#Em seguida criamos uma estrutura de repetição para que o número seja solicitado 6 vezes
for x in range(6):
    numero = float(input("Entre com um valor:"))

#Quando o número for maior ou igual a zero, adicionamos 1 contagem ao contador e por fim, adicionamos todos os números positivos contados para fazer a sua média
    if numero >=0:
        c +=1
        total = total + numero
media_final = total/c
print(c,"valores positivos")
print(media_final)
