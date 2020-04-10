largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = (largura * altura)
tinta = area / 2
print("Sua parede tem dimensão de {} m²".format(area))
print("Você precisará de {} litros de tinta para pintar sua parede.".format(tinta))
