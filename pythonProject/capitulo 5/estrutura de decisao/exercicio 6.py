

def contaImpares(n1, n2, n3, n4):
    total = 0

    if (n1 % 1 == 0):
        total += 1
    if (n2 % 1 == 0):
        total += 1
    if (n3 % 1 == 0):
        total += 1
    if (n4 % 1 == 0):
        total += 1

    return total



def contaPares(n1, n2, n3, n4):
    total = 0

    if (n1 % 2 == 0):
        total += 1
    if (n2 % 2 == 0):
        total += 1
    if (n3 % 2 == 0):
        total += 1
    if (n4 % 2 == 0):
        total += 1

    return total


n1 = int(input("Digite a primeira numero: "))
n2 = int(input("Digite a segunda numero: "))
n3 = int(input("Digite a terceira numero: "))
n4 = int(input("Digite a quarta numero: "))


print(f"São: {contaImpares(n1,n2,n3,n4)} numeros impares")
print(f"São: {contaPares(n1, n2, n3, n4)} numeros pares")

contaImpares(n1, n2, n3, n4)
contaPares(n1,n2,n3,n4)