print("\n****  CALCULADORA DE CALORIAS DIÁRIAS  ****")
quantidade_alimento = int(input("\nDigite a quantidade de alimentos ingeridos no seu dia: "))
soma = 0

for x in range(1, quantidade_alimento+1):
    calorias_alimentos = float(input("Informe a quantidade de calorias do alimento {}: ".format(x)))
    soma = soma + calorias_alimentos
print("\n O TOTAL DE CALORIAS INGERIDAS É DE: {} Kcal".format(soma))





