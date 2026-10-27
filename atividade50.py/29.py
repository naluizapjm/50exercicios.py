numero_secreto = 15

while True:
    tentativa = int(input("Adivinhe o número entre 1 e 20: "))

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif tentativa > numero_secreto:
        print("O número secreto é menor!")
    else:
        print("O número secreto é maior!")