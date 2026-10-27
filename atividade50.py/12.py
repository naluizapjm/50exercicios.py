while True:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 4:
        print("Saindo do programa...")
        break

    if opcao >= 1 and opcao <= 3:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado:", numero1 + numero2)
        elif opcao == 2:
            print("Resultado:", numero1 - numero2)
        elif opcao == 3:
            print("Resultado:", numero1 * numero2)
    else:
        print("Opção inválida!")