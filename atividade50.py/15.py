voto1 = 0
voto2 = 0
voto3 = 0

while True:
    print("\n1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("0 - Encerrar votação")

    voto = int(input("Digite seu voto: "))

    if voto == 0:
        break
    elif voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    else:
        print("Voto inválido!")

print("Total de votos:")
print("Opção 1:", voto1)
print("Opção 2:", voto2)
print("Opção 3:", voto3)