valor = int(input('\n - Digite o número que gostaria de saber a tabuada: '))
n = 0

print("SEGUE A TABUADA DO {}:".format(valor))

while n <= 10:
    print("{0} X {1} = {2}".format(valor, n, (n * valor)))
    n = n + 1
