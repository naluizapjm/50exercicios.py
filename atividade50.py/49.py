produtos = []

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Buscar produto")
    print("3 - Listar produtos")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))

        produtos.append([nome, quantidade])

    elif opcao == 2:
        busca = input("Digite o nome do produto: ")
        encontrou = False

        for produto in produtos:
            if produto[0].lower() == busca.lower():
                print("Produto:", produto[0])
                print("Quantidade:", produto[1])
                encontrou = True
                break

        if not encontrou:
            print("Produto não encontrado!")

    elif opcao == 3:
        ordenados = []

        for produto in produtos:
            ordenados.append(produto)

        for i in range(len(ordenados)):
            for j in range(len(ordenados) - 1 - i):
                if ordenados[j][0].lower() > ordenados[j + 1][0].lower():
                    ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]

        for produto in ordenados:
            if produto[1] <= 0:
                continue

            print(produto[0], "-", produto[1], "unidades")

    elif opcao == 4:
        break

    else:
        print("Opção inválida!")