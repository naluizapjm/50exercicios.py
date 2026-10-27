numero = int(input("Digite um número (0 para parar): "))

maior = numero

while numero != 0:
    if numero > maior:
        maior = numero

    numero = int(input("Digite outro número (0 para parar): "))

if maior == 0:
    print("Nenhum número foi informado.")
else:
    print("O maior número informado foi:", maior)