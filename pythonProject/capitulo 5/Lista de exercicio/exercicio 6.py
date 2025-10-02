


def calculaMediaBimestral (n1,n2,n3,n4):
    mediaFormativa = (n1 + n2 + n3 / 3.0)
    totalBimestral = n4 * 0.7
    mediaBimestral = ((mediaFormativa * 0.3) + totalBimestral)
    print(f"A média é {mediaBimestral}")




n1 = float(input("A nota da primeira: "))
n2 = float(input("A nota da segunda: "))
n3 = float(input("A nota da terceira: "))
n4 = float(input("Nota da prova bimestral: "))


calculaMediaBimestral(n1,n2,n3,n4)