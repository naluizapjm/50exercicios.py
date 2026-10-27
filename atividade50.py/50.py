numeros = []

for contador in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

while True:
    print("\n1 - Calcular média")
    print("2 - Maior e menor número")
    print("3 - Ordem crescente")
    print("4 - Ordem decrescente")
    print("5 - Busca linear")
    print("6 - Busca binária")
    print("7 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        media = sum(numeros) / len(numeros)
        print("Média:", media)

    elif opcao == 2:
        maior = numeros[0]
        menor = numeros[0]

        for numero in numeros:
            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero

        print("Maior:", maior)
        print("Menor:", menor)

    elif opcao == 3:
        print("Ordem crescente:", sorted(numeros))

    elif opcao == 4:
        print("Ordem decrescente:", sorted(numeros, reverse=True))

    elif opcao == 5:
        busca = int(input("Digite o número que deseja procurar: "))
        comparacoes = 0
        encontrou = False

        for numero in numeros:
            comparacoes += 1

            if numero == busca:
                encontrou = True
                break

        print("Encontrado:", encontrou)
        print("Comparações:", comparacoes)

    elif opcao == 6:
        lista = sorted(numeros)

        busca = int(input("Digite o número que deseja procurar: "))

        inicio = 0
        fim = len(lista) - 1
        comparacoes = 0
        encontrou = False

        while inicio <= fim:
            meio = (inicio + fim) // 2
            comparacoes += 1

            if lista[meio] == busca:
                encontrou = True
                break
            elif lista[meio] < busca:
                inicio = meio + 1
            else:
                fim = meio - 1

        print("Encontrado:", encontrou)
        print("Comparações:", comparacoes)

    elif opcao == 7:
        break

    else:
        print("Opção inválida!")