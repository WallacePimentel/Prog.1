#Iremos definir os dados de entrada

Funcionario = int(input("Digite o número do funcionário:"))

Horas = int(input("Digite a quantidade de horas trabalhadas: "))
SPHora = float(input("Digite o valor por hora que o funcionário recebe: "))
#SPHora = Salário por hora

#Calcularemos o salário total de um funcionário multiplicando a quantidade de horas trabalhadas pelo quanto ele ganha por hora.

Salario = (Horas * SPHora)

print("O funcionário de número", Funcionario, "deve receber R$", Salario)