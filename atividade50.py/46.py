numeros = []

for contador in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(len(numeros)):
    menor = i

    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[menor]:
            menor = j

    numeros[i], numeros[menor] = numeros[menor], numeros[i]

print("Números ordenados:", numeros)