print("\n ***** CALCULADORA CONTAGEM DE ACESSOS AO SISTEMA (MANUALMENTE) *****")
maior_quantidade_digitada = 0

limite_superior = int(input("\n Qual o número de usuários que acessam o sistema? "))

for usuario in range (1,limite_superior+1):
    total_de_acessos = int(input("\n Digite o seu número de acessos do usuário {}: ".format(usuario)))

    if (total_de_acessos > maior_quantidade_digitada):
       maior_quantidade_digitada = total_de_acessos

print("\n O usuário que teve mais acessos, acessou o sistema {} vezes.".format(maior_quantidade_digitada))
