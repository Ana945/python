def calculaIMC(altura):
    media = 62.1
    base = 44.7
    return media * altura - base
#main

altura = float(input("Digite sua altura: "))

imc = calculaIMC(altura)

print(f"O peso ideal da mulher é: {imc}")