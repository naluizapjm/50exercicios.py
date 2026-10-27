alunos = []

for contador in range(10):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

busca = input("Digite o nome que deseja procurar: ")

encontrou = False

for aluno in alunos:
    if aluno.lower() == busca.lower():
        encontrou = True
        break

if encontrou:
    print("Aluno cadastrado!")
else:
    print("Aluno não encontrado!")