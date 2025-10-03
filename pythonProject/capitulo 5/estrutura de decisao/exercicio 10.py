
def categoria(idade):
    if (idade >= 5):
        if (idade <= 7):
            print("infantil A")

    if (idade >= 8):
        if (idade <= 10):
            print("infantil B")

    if (idade >= 11):
        if (idade <= 13):
            print("juvenil A")

    if (idade >= 14):
        if (idade <= 17):
            print("juvenil B")

    if (idade >= 18):
        print("É senior")

idade = int(input("Qual sua idade: "))

categoria(idade)