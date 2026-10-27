numeros = []

for contador in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

menor = numeros[0]
indice_menor = 0

for indice in range(1, len(numeros)):
    if numeros[indice] < menor:
        menor = numeros[indice]
        indice_menor = indice

print("Menor valor:", menor)
print("Índice:", indice_menor)