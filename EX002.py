print("Qual é o seu plano: ")
print("B = Basic")
print("S = Silver")
print("G = Gold")
print("P = Platium")

assinatura = input("Insira a PRIMEIRA LETRA do seu plano: ").upper()
faturamento = input("Insira o faturamento: ")
faturamento = float(faturamento)

if assinatura == "B":
    total_pagamento = faturamento * 30 / 100
    print("O valor do bônus a pagar é de: {:.2f} R$ ".format(total_pagamento))
elif assinatura == "S":
    total_pagamento = faturamento * 20 / 100
    print("O valor do bônus a pagar é de: {:.2f} R$ ".format(total_pagamento))
elif assinatura == "G":
    total_pagamento = faturamento * 10 / 100
    print("O valor do bônus a pagar é de: {:.2f} R$ ".format(total_pagamento))
elif assinatura == "P":
    total_pagamento = faturamento * 5 / 100
    print("O valor do bônus a pagar é de: {:.2f} R$ ".format(total_pagamento))