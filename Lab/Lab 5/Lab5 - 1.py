#Aqui solicitamos a lista, o número a ser encontrado e criamos um contador
n = input("Entre com uma lista: ").split()
contador = 0
procura = input()

#Aqui verificamos quais termos da lista são iguais ao elemento procurado, e a cada
#ocorrência dessa, adicionamos 1 ao contador
for i in range(len(n)):
    if n[i] == procura:
        contador += 1
print("O elemento",procura,"aparece",contador,"vezes")