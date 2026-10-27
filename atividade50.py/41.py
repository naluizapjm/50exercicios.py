numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
           22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

busca = int(input("Digite um número para procurar: "))

inicio = 0
fim = len(numeros) - 1
encontrou = False

while inicio <= fim:
    meio = (inicio + fim) // 2

    if numeros[meio] == busca:
        encontrou = True
        break
    elif numeros[meio] < busca:
        inicio = meio + 1
    else:
        fim = meio - 1

if encontrou:
    print("Número encontrado!")
else:
    print("Número não encontrado!")