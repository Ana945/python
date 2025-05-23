num = int(input("Escolha um numero de cinco digitos: "))

digito1 = num // 10000
digito2 = (num % 10000) // 1000
digito3 = (num % 1000) // 100
digito4 = (num % 100) // 10
digito5 = num % 10

print(digito1)
print(digito2)
print(digito3)
print(digito4)
print(digito5)