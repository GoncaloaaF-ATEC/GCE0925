"""
Com a materia ja falada

faça um programa que receba um num e devolva o mes correspondente:
1 - Jan
2 - Fev
3 - Mar
4 - Abr
5 - Mai
...
12 - Dez

outro valor - Mes invalido

"""
from unittest import case

mes = int(input("indique o numero do mes: "))

if mes == 1:
    print(f"Jan")
elif mes == 2:
    print(f"Fev")
elif mes == 3:
    print(f"Mar")
elif mes == 4:
    print(f"Abr")
elif mes == 5:
    print(f"Mai")
elif mes == 6:
    print(f"Jun")
elif mes == 12:
    print(f"Dez")
else:
    print("invalido")

print("---------------")

mes = int(input("indique o numero do mes: "))
match mes:
    case 1:
        print("Jan")
    case 2:
        print("Fev")
    case 3:
        print("Mar")
    case 4:
        print("Abr")
    case 5:
        print("Mai")
    case 6:
        print("Jun")
    case 12:
        print("Dez")
    case _:
        print("invalido")




"""
Com a materia ja falada

faça um programa que receba um num e devolva o mes dia da semana correspondente:

1 - dom
2 - segunda
3 - terça
4 - quarta
5 - quinta
6 - sexta
7 - sabado
8 - invalido

outro valor - Mes invalido

"""