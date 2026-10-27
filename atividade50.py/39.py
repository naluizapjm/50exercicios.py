numeros = []

for contador in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maior = numeros[0]
indice_maior = 0

for indice in range(1, len(numeros)):
    if numeros[indice] > maior:
        maior = numeros[indice]
        indice_maior = indice

print("Maior valor:", maior)
print("Índice:", indice_maior)