numeros = []

for contador in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

numeros_ordenados = sorted(numeros)

print("Ordem crescente:", numeros_ordenados)