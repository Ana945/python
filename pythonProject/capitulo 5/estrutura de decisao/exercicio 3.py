
def numeroMaior(v1, v2, v3):
    if (v1 > v2):
        if (v1 > v3):
            print("esse", v1 ,"é o maior numero")

    if (v2 > v1):
        if (v2 > v3):
            print("esse", v2 ,"é o maior")

    if (v3 > v1):
        if (v3 > v2):
            print("esse", v3 ,"é o maior")


v1 = int(input("insira um valor: "))
v2 = int(input("insira um valor: "))
v3 = int(input("insira um valor: "))

numeroMaior(v1, v2, v3)