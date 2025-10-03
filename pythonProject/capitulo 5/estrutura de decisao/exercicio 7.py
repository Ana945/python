def verificaValor(n1):


    if(n1 == 0):
        print("É zero")

    if(n1 >= 0):
       print("Seu numero é positivo")
    else:
        print("Seu numero é negativo")


n1 = int(input("Digite um numero: "))

verificaValor(n1)