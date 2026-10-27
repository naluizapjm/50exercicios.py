idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 120:
    print("Idade inválida!")
    idade = int(input("Digite sua idade novamente: "))

print("Idade válida:", idade)