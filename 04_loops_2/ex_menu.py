"""

Crie um menu com 4 opções
sendo a 4 para terminar

caso seja inserida uma opção invalida deve indicar que a opção e invalida


"""

while True:
    print("------Menu-------")
    print("| opt1        1 |")
    print("| opt2        2 |")
    print("| opt3        3 |")
    print("| Sair        0 |")
    print("-----------------")
    opt = input("Escolha a opção: ")

    match opt:
        case "1":
            print("opt1")
        case "2":
            print("opt2")
        case "3":
            print("opt3")
        case "0":
            print("Sair")
            break
        case _:
            print("opçao invalida")

