soma = 0
quantidade = 0

nota = float(input("Digite uma nota (-1 para parar): "))

while nota != -1:
    soma += nota
    quantidade += 1

    nota = float(input("Digite uma nota (-1 para parar): "))

if quantidade > 0:
    media = soma / quantidade
    print("A média das notas é:", media)
else:
    print("Nenhuma nota foi informada.")