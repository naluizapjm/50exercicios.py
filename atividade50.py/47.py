numeros = []

for contador in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(1, len(numeros)):
    atual = numeros[i]
    j = i - 1

    while j >= 0 and numeros[j] > atual:
        numeros[j + 1] = numeros[j]
        j -= 1

    numeros[j + 1] = atual

    print("Lista após inserção:", numeros)

print("Lista final:", numeros)