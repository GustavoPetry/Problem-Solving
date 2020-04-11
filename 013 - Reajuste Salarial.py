salario = float(input("Digite o salário do funcionário: "))
porcentagem = float(input("Digite o número da porcentagem do reajuste salarial: "))

calc1 = (salario * porcentagem)/100
calc2 = salario + calc1

print("O funcionário que ganhava R$ {}, com {}% de aumento, passa a receber R$ {}".format(salario, porcentagem, calc2))
