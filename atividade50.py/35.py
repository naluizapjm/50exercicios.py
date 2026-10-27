nomes = []

for contador in range(10):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Nomes que não começam com A:")

for nome in nomes:
    if nome.upper().startswith("A"):
        continue

    print(nome)