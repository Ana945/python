def soma(n1, n2, n3, n4):
    total = 0

    if(n1 % 2 == 0):
        total += n1
    if (n2 % 2 == 0):
        total += n2
    if (n3 % 2 == 0):
        total += n3
    if (n4 % 2 == 0):
        total += n4

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

def main():
    n1 = int(input("Digite a primeira numero: "))
    n2 = int(input("Digite a segunda numero: "))
    n3 = int(input("Digite a terceira numero: "))
    n4 = int(input("Digite a quarta numero: "))

    totalSoma = soma (n1, n2, n3, n4)
    totalPares = contaPares(n1, n2, n3, n4)
    media = totalSoma / totalPares
    print(f"a soma dos numeros é: {totalSoma}")
    print(f"A média dos numeros é: {media}")

if __name__ == "__main__":
        main()