soma = 0

for contador in range(10):
    numero = int(input("Digite um número: "))

    if numero < 0:
        continue

    soma += numero

print("Soma dos números não negativos:", soma)