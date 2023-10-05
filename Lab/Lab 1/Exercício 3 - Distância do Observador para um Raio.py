#Aqui estamos definindo a velocidade do som e exigindo o tempo demorado para o usuário ouvir o som

tempo = float(input("Digite o tempo percorrido (em segundos) entre ver e ouvir o raio: "))
velocidade = 340

#Aqui calculamos a distancia multiplicando o tempo pela velocidade
distancia = float(tempo * velocidade)

print("Como o tempo de ouvir o trovão foi", tempo, "o raio caiu a ", distancia, "metros daqui.")