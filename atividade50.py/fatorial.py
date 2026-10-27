numero = int(input("Digite um número inteiro não negativo: "))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print("O fatorial é:", fatorial)