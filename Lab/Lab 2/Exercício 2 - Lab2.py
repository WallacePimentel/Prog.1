#Aqui estamos exigindo o valor de entrada do usuário
valor = float(input("Entre com o um número real: "))

#Aqui estamos comparando para ver em que intervalo o valor que o usuário inseriu se encaixa
if 0 <= valor <= 25:
    print("O valor está entre o intervalo [0,25]")
elif 25 < valor <= 50:
    print("O valor está entre o intervalo (25,50]")
elif 50 < valor <= 75:
    print("O valor está entre o intervalo (50,75]")
elif 75 < valor <= 100:
    print("O valor está entre o intervalo (75,100]")
else:
    print("Valor fora de intervalo.")

