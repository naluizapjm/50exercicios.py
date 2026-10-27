base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for contador in range(expoente):
    resultado *= base

print("Resultado:", resultado)