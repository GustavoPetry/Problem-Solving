print("\n Qual unidade gostaria de converter? \n 1 - milímetros (mm) \n 2 - centímetros (cm) \n 3 - metros (m) \n 4 - quilômetros (km)")
opcao = int(input("\nESCOLHA UMA OPÇÃO: "))


if opcao == 1:
    escolha = float(input("Digite quantos MILÍMETROS irá converter: "))
    cm = escolha / 10
    m = escolha / 1000
    km = escolha / 1000000
    print("Conversões do valor {} milímetros:\n - Centímetros = {} cm\n - Metros = {} m\n - Quilômetros = {:.10f} km".format(escolha, cm, m, km))

elif opcao == 2:
    escolha = float(input("Digite quantos CENTÍMETROS irá converter: "))
    mm = escolha * 10
    m = escolha / 100
    km = escolha / 100000
    print(
        "Conversões do valor {} centímetros:\n - milímetros = {} mm\n - Metros = {} m\n - Quilômetros = {:.10f} km".format(escolha, mm, m, km))

elif opcao == 3:
    escolha = float(input("Digite quantos METROS irá converter: "))
    mm = escolha * 1000
    cm = escolha * 100
    km = escolha / 1000
    print("Conversões do valor {} metros:\n - Milímetros = {} mm\n - Centímetros = {} cm\n - Quilômetros = {:.10f} km".format(escolha, mm, cm, km))

elif opcao == 4:
    escolha = float(input("Digite quantos QUILÔMETROS irá converter: "))
    mm = escolha * 1000000
    cm = escolha * 100000
    m = escolha * 1000
    print("Conversões do valor {} quilômetros:\n - Milímetros = {} mm\n - Centímetros = {} cm\n - Metros = {} m".format(escolha, mm, cm, m))

else:
    print("Comando inválido, tente novamente.")
