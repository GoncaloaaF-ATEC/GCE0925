"""
Crie um menu para poder selecionar um dos ex anteriores de forma a
 poder selecionar um para executar

"""

while True:
    print("------Menu-------")
    print("| ex1         1 |")
    print("| ex2         2 |")
    print("| ex3         3 |")
    print("| Sair        0 |")
    print("-----------------")
    opt = input("Escolha a opção: ")

    match opt:
        case "1":

            ano_curr = 2025

            ano = int(input("ano de nascimento: "))

            idade = ano_curr - ano

            if idade >= 18:
                print(f"Adulto - {idade}")
            elif idade >= 12:
                print(f"Adolescente - {idade}")
            else:
                print(f"criança - {idade}")

            input("pressione <enter> para continuar")
        case "2":

            num1 = int(input("num1: "))
            num2 = int(input("num2: "))
            num3 = int(input("num3: "))

            if num1 > 20:
                print(f"opt1")
            elif num2 > 30:  # sei q num1 <= 20
                print(f"opt2")
            else:
                print(f"opt3")

            input("pressione <enter> para continuar")

        case "3":
            num = int(input('num: '))
            aux = 0

            while aux <= num:
                print(aux, end=' ')
                aux += 1
            print("")
            input("pressione <enter> para continuar")

        case "0":
            print("Sair")
            break
        case _:
            print("opçao invalida")
            input("pressione <enter> para continuar")

