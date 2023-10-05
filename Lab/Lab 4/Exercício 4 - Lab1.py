#Primeiro requisitamos o valor do usuário em centavos
print("\033c")

valor = int(input("Digite o valor em centavos: "))

#Após fizemos uma série de operações em que dividimos o valor total pelo valor da maior moeda
#Utilizamos o resto para dividir pelo valor da próxima moeda e assim em diante até chegar a menor moeda
v100 = (valor // 100)
r100 = (valor % 100)

v50 = (r100 // 50)
r50 = (r100 % 50)

v25 = (r50 // 25)
r25 = (r50 % 25)

v10 = (r25 // 10)
r10 = (r25 % 10)

v5 = (r10 // 5)
r5 = (r10 % 5)

v1 = (r5 // 1)

#Aqui exibimos o quantidade utilizada de cada moeda em ordem
print("Para o valor de: ", valor,
      "\n", v100, "moedas de 1 real",
      "\n",v50, "moedas de 50 centavos",
          "\n",v25, "moedas de 25 centavos",
              "\n",v10, "moedas de 10 centavos",
                  "\n",v5, "moedas de 5 centavos",
                      "\n",v1, "moedas de 1 centavo.")
