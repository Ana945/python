def calculaDiametro(raio):
    return 2 * raio

def calculaCircunferencia(raio, pi):
    return (2 * raio) * pi

def calculaAreaCircunferencia(pi, raio):
    return pi * (raio ** 2)

#main
raio = int(input("Digite o valor do raio: "))
pi = 3.14159

diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(raio, pi)
areaCircunferencia = calculaAreaCircunferencia(pi, raio)

print("O valor do diametro é: ", diametro)
print("O valor da circunferencia é: ", circunferencia)
print("O valor da area da circunferencia é: ", areaCircunferencia)

