

def tabela(codigo):
    if (codigo == 1):
        print("Alimento não-perecível")

    if (codigo >= 2):
        if (codigo <= 4):
            print("Alimento perecível")

    if (codigo >= 5):
        if (codigo <= 6):
            print("Vestuário")

    if (codigo == 7):
        print(" Higiene pessoal")

    if (codigo >= 8):
        if (codigo <= 15):
            print("iLimpeza e utensílios domésticos")

    if (codigo > 18):
        print("Invalido")


codigo = int(input("Código do produto: "))

tabela(codigo)