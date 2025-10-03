def verifica(n1):
    if (n1 % 5 == 0):
        print(f"{n1} é dividido por 5")

    elif (n1 % 3 == 0):
        print(f"{n1} é dividido por 3 ")

    else:
        print(f"O numero {n1} não é divisivel por 5 nem 3")


n1 = int(input("Digite um numero inteiro: "))

verifica(n1)