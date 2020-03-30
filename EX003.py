print("Digite a quantidade de votos dos dias da semana para assistir a live: ")

segunda_feira: int = int(input("Segunda-feira: "))
terca_feira: int = int(input(("Terça-feira: ")))
quarta_feira: int = int(input("Quarta-feira: "))
quinta_feira: int = int(input("Quinta-feira: "))
sexta_feira: int = int(input("Sexta-feira: "))

dia_mais_votado: str = ""
if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    dia_mais_votado = "Segunda-feira"
elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira:
    dia_mais_votado = "Terça-feira"
elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    dia_mais_votado = "Quarta-feira"
elif quinta_feira >  segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
    dia_mais_votado = "Quinta-feira"
elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
    dia_mais_votado = "Sexta-feira"
else:
    print("Tivemos um empate!")
    exit (0)
print("O dia mais votado para assitir a live foi: {}".format(dia_mais_votado))





