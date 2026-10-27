saldo = 0

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
        else:
            print("Valor inválido!")

    elif opcao == 2:
        valor = float(input("Valor do saque: "))

        if valor > 0 and valor <= saldo:
            saldo -= valor
        else:
            print("Saque inválido!")

    elif opcao == 3:
        print("Saldo atual:", saldo)

    elif opcao == 4:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")