while True:
    numero = int(input("Digite um número positivo: "))

    if numero > 0:
        break

    print("Número inválido! Tente novamente.")

print("Número válido:", numero)