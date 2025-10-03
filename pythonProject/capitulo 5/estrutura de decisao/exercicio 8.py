

def verifica(n1):

        if(n1 % 2 == 0):
            print(f"{n1} é dividido por 2")

        elif (n1 % 3 == 0):
            print(f"{n1} é dividido por 3 ")

        else: print(f"O numero {n1} não é divisivel por 2 nem 3")



n1 = int(input("Digite um numero inteiro: "))


verifica(n1)