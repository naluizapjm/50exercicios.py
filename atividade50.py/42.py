numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
           22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

busca = int(input("Digite um número para procurar: "))

comparacoes_linear = 0
encontrou_linear = False

for numero in numeros:
    comparacoes_linear += 1

    if numero == busca:
        encontrou_linear = True
        break

inicio = 0
fim = len(numeros) - 1
comparacoes_binaria = 0
encontrou_binaria = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    comparacoes_binaria += 1

    if numeros[meio] == busca:
        encontrou_binaria = True
        break
    elif numeros[meio] < busca:
        inicio = meio + 1
    else:
        fim = meio - 1

print("Busca linear:", comparacoes_linear, "comparações")
print("Busca binária:", comparacoes_binaria, "comparações")

print("Encontrado na busca linear:", encontrou_linear)
print("Encontrado na busca binária:", encontrou_binaria)