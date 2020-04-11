dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilômetros foram percorridos com o carro? "))

calculo_dias = dias * 60
calculo_km = km * 0.15
total = calculo_dias + calculo_km

print("O total a pagar é de: R$ {}".format(total))
