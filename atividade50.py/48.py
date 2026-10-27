alunos = []

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Pesquisar aluno")
    print("3 - Listar alunos")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do aluno: ")

        notas = []

        for contador in range(2):
            nota = float(input("Digite uma nota: "))
            notas.append(nota)

        media = sum(notas) / len(notas)

        aluno = [nome, notas, media]
        alunos.append(aluno)

        print("Aluno cadastrado!")

    elif opcao == 2:
        busca = input("Digite o nome do aluno: ")
        encontrou = False

        for aluno in alunos:
            if aluno[0].lower() == busca.lower():
                print("Nome:", aluno[0])
                print("Notas:", aluno[1])
                print("Média:", aluno[2])
                encontrou = True
                break

        if not encontrou:
            print("Aluno não encontrado!")

    elif opcao == 3:
        for aluno in alunos:
            print("Nome:", aluno[0], "| Média:", aluno[2])

    elif opcao == 4:
        break

    else:
        print("Opção inválida!")