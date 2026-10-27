soma = 0

for contador in range(10):
    nota = float(input("Digite a nota do aluno: "))

    if contador == 0:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

    soma += nota

media = soma / 10

print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média da turma:", media)