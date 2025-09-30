nota1 = 9
nota2 = 9


if nota1 >= 10 and nota2 >= 10:
    print("Aprovado")
elif nota1 >= 10 or nota2 >= 10:
    print("recuperação")
else:
    print("Reprovado")



"""
    faça um porgrama onde é pedido ao utlizador 3 numeros: num1, num2, num3

    se num2 > 30 e num1 <= 20 - escreva na consola opt2
    se não se num1 > 20 - escreva na consola opt1
    se nao imprima - opt3

    deve usar o if, elif else
"""

num1 = 9
num2 = 9
num3 = 9

if num1 >= 30 and num2 <= 20:
    print("opt2")
elif num1 > 20 :
    print("opt1")
else:
    print("opt3")
