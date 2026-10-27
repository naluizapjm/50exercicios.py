numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

busca = int(input("Digite um número para procurar: "))

encontrou = False

for numero in numeros:
    if numero == busca:
        encontrou = True
        break

if encontrou:
    print("Número encontrado!")
else:
    print("Número não encontrado!")