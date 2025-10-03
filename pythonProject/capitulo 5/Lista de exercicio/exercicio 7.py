
def calculaKmLitro(kmInicial,kmFinal, litros):
    calculoTotalKm = kmFinal - kmInicial / litros
    print(f"O consumo dos seu km é: {calculoTotalKm}")


def calculaLucro(preco, valorTotal, litros):
    calculoTotalLucro = valorTotal - (litros * preco)
    print(f"Lucro líquido do dia é: {calculoTotalLucro}")


preco = float(input("o preço do combustível: "))
kmInicial = float(input("a marcação do odômetro no inicio: "))
kmFinal = float(input("a marcação do odômetro no final: "))
litros = float(input("litros de combustível gasto: "))
valorTotal = float(input("valor total recebido dos passageiros: "))



calculaKmLitro(kmInicial,kmFinal, litros)
calculaLucro(preco, valorTotal, litros)
