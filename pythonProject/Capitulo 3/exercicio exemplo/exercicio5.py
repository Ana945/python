def calculoDaMedia(nota1, nota2, nota3, nota4):
    resultado_nota = (nota1 + nota2 + nota3 + nota4) / 4
    print("Sua média é: ", resultado_nota)


nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media = calculoDaMedia(nota1, nota2, nota3, nota4)
