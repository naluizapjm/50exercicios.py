soma = 0

for numero in range(1, 101):
    if numero % 2 == 0:
        soma += numero

print("Soma dos números pares:", soma)