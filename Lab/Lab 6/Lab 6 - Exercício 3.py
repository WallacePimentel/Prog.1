#Dupla: Wallace da Rocha Pimentel Júnior e Gabriel Rocha dos Santos

# Aqui estamos coletando a quantidade de dados que o usuário quer 
dados = int(input("Entre com a quantidade de dados: "))
# Aqui estamos iniciando 4 listas que irão receber a frequência e o identificador do dado, a quantidade total
# de graus de um determinado dado (frequência do dado * 360) e o resultado final esperado
frequencia = []
titulo = []
graus = []
resultados = []
# Aqui estamos iniciando uma variável para receber a soma de todas as frequências dos dados
dividendo = 0

# Aqui estamos pegando cada identificador e frequência do dado para todas as quantidades de dados informadas
# inicialmente
for i in range(dados):
    d = input(f"Entre com o identificador do dado {i+1}: ")
    titulo.append(d)
    n = int(input(f"Entre com a frequencia do dado {d}: "))
    frequencia.append(n)
    graus.append(n * 360)

# Aqui estamos pegando a soma de todas as frequências dos dados
for h in frequencia:
    dividendo += h

# Aqui estamos fazendo o calculo da (frequência do dado * 360)/total das frequencias dos dados e armazenando 
# na lista "resultados"
for x in graus:
    resultados.append(x / dividendo)

# Aqui estamos imprimindo o resultado esperado
print("Mapeamento:")
for z in range(len(resultados)):
    print(f"[{titulo[z]} : {resultados[z]}]")