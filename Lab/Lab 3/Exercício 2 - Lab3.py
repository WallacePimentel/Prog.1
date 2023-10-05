#Aqui estamos exigindo uma decisão do usuário e enquanto o usuário entra com Sim, para que repita a pergunta e execute o processo novamente com o número digitado
decisao = input("Deseja entrar com um número (S/N)?")
while decisao == "S":
    c = 0
    numero = int(input("Entre com um número:"))
    print("Divisores de", numero,":" )

#Aqui estamos vendo todos os divisores pelos quais a divisão do número por eles resulta em 0 e contando quantas vezes isso ocorre
    for x in range(1,numero+1):
        resto_divisao = numero % x
        if resto_divisao == 0:
            c += 1
            print(x)
#Se o número possuir somente 2 divisores ele é primo
    if c == 2:
        print("O número é primo.")
    decisao = input("Deseja entrar com um número (S/N)?")