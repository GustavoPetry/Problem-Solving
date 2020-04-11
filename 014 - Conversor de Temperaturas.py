print(" 1 - Converter Celsus para Fahrenheit \n 2 - Converter Fahrenheit para Celsus")
escolha = int(input("Escolha uma das opções: "))

while escolha == 1:
    celsus = float(input("Informe a temperatura em Celsus: "))
    calculo1 = celsus * (9/5) + 32
    print("A temperatura é de {:.2f} °F".format(calculo1))

if escolha == 2:
    fahrenheit = float(input("Informe a temperatura em fahrenheit: "))
    calculo2 = (fahrenheit - 32) * 5/9
    print("A temperatura é de {:.2f} °C".format(calculo2))

else:
    print("\n ***** Comando inválido! Tente novamente. *****")