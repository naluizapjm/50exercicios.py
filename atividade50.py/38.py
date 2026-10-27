numeros = [5, 10, 15, 20, 25, 30, 35, 40]

busca = int(input("Digite um número: "))

encontrou = False

for indice in range(len(numeros)):
    if numeros[indice] == busca:
        print("Número encontrado no índice:", indice)
        encontrou = True
        break

if not encontrou:
    print("Número não encontrado!")