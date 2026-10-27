senha_correta = "python123"
tentativas = 0

while tentativas < 3:
    senha = input("Digite sua senha: ")

    if senha == senha_correta:
        print("Acesso autorizado!")
        break
    else:
        tentativas += 1
        print("Senha incorreta!")

if tentativas == 3:
    print("Acesso bloqueado!")