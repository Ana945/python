def soma(numero, numero2):
    print("O resultado da adição é: ", numero + numero2)

def subtracao(numero, numero2):
    print("O resultado da subtração é: ", numero - numero2)

def multiplicacao(numero, numero2):
    print("o resultado da multiplicação é: ", numero * numero2)

def divisao(numero, numero2):
    resultado_divisao= numero/numero2
    print("O resultado é: ", resultado_divisao)

numero = int(input("Digite o 1° numero:"))
numero2 = int(input("Digite o 2° numero:"))

soma(numero, numero2)
subtracao(numero, numero2)
multiplicacao(numero, numero2)
divisao(numero, numero2)