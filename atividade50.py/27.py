estoque = int(input("Digite a quantidade inicial do estoque: "))

while estoque > 0:
    print("Estoque disponível:", estoque)

    retirada = int(input("Quantos produtos deseja retirar? "))

    if retirada <= 0:
        print("Quantidade inválida!")
    elif retirada > estoque:
        print("Retirada maior que o estoque disponível!")
    else:
        estoque -= retirada

print("Estoque zerado!")