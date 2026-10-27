soma = 0

for contador in range(5):
    nota = float(input("Digite uma nota: "))
    soma += nota

media = soma / 5

print("Média:", media)

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")