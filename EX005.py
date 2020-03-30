print("\n******   SISTEMA DE NOTAS DA ESCOLA DE INGLÊS JOWELL SANT'ANA   ******")
print("\n -- Digite as notas dos alunos com o número de chamada ímpar -- ")

contador_impar = 1
somanotas_impar = 0

for contador_impar in range(1,50,2):
    notas_impar = str(input("Insira a nota do aluno {}: ".format(contador_impar)))
    contador_impar = contador_impar + 2
    notas_impar = notas_impar.replace(",", ".")
    somanotas_impar = float(somanotas_impar) + float(notas_impar)

media_impar = float(somanotas_impar/25)

print("\nA média da nota dos alunos ímpares da sala é de: {} ".format(media_impar))
print(("\n --- Agora vamos calcular as notas dos alunos pares --- "))

contador_par = 2
somanotas_par = 0

for contador_par in range(1,51,2):
        notas_par = str(input("Insira a nota do aluno {}: ".format(contador_par)))
        contador_par = contador_par + 2
        notas_par = notas_par.replace(",", ".")
        somanotas_par = float(somanotas_par) + float(notas_par)

media_par  = float (somanotas_par/25)

print("A média das notas dos alunos da sala é de: {}".format((media_par)))


