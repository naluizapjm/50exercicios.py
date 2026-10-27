alunos = []

while True:
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")

    if continuar == "n":
        break

print("Alunos cadastrados:")

for aluno in alunos:
    print(aluno)