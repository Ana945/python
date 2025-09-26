def validaIdade(idade):
    if(idade >= 18):
        print("Você é maior de idade ")

    else:
        print("Você é menor idade ")

idade = int(input("Digite a sua idade: "))

validaIdade(idade)