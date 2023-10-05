#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

# Aqui estamos criando a matriz que receberá o tabuleiro final do jogo da velha e a variável ganhador
matriz = []
ganhador = 0

# Aqui estamos coletando o tabuleiro final do jogo e armazenando em "matriz"
print("Entre com o jogo:")
for i in range(3):
    linha = input().split()
    matriz.append(linha)

# Aqui estamos analisando cada situação que leva a vitória de um determinado jogador e anotando qual é o 
# ganhador caso exista
for h in range(3):
    if matriz[h][0] == matriz[h][1] == matriz[h][2]:
        ganhador = matriz[h][0]

    elif matriz[0][h] == matriz[1][h] == matriz[2][h]:
        ganhador = matriz[0][h]

    elif matriz[0][0] == matriz[1][1] == matriz[2][2]:
        ganhador = matriz[0][0]

    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
        ganhador = matriz[0][2]

# Aqui estamos imprimindo o ganhador ou se é empate.
if ganhador != 0:
    print(f"{ganhador} é o vencedor")
else:
    print("Empate")