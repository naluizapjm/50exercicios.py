numeros = []

for contador in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(len(numeros)):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Números em ordem crescente:", numeros)