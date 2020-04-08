minuto = int(input('Digite o minuto atual: '))
t = minuto + 1
fatorial = 0

for senha in range(1, minuto):
    minuto = minuto * senha
print("A senha é LIBERDADE{}".format(minuto))

