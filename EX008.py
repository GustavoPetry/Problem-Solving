# Variáveis
notas = []
opcao = -1

# Quando a opção for diferente de 3 faça:
while opcao != 3:
    print(" \n 1 - INFORMAR NOTAS \n 2 - EXIBIR AS NOTAS INFORMADAS \n 3 - CALCULAR MÉDIA DAS NOTAS INFORMADAS \n 4 - SAIR DO SISTEMA ")
    opcao = int(input("\n ESCOLHA SUA OPÇÃO: "))

# Se...
    if opcao == 1:
        notas.append(float(input("DIGITE A NOTA: ")))
# ...
    elif opcao == 2:
        for x in notas:
            print(x)
    elif opcao == 3:
        print(sum(notas) / len (notas))
    elif opcao == 4:
        print("\n **** O SISTEMA SENDO ENCERRADO ****")
#Senão...
    else:
        print("\n **** COMANDO INVÁLIDO, TENTE NOVAMENTE! ****")



