"""
faça um porgrama onde é pedido ao utlizador um ano de nascimento,
 com base no ano deve calcular a idade (pode assumir que o ano atual e 2025)
 - se tiver mais de 18 anos deve indicar adulto,
 - se tiver entre 12 e 18 deve indicar adolescente
 - se tiver menos de 12 deve indicar criança

deve usar o if, elif else
"""

ano_curr = 2025 # anocurr -> ma pratica | ano_curr -> boa pratica

ano = int(input("ano de nascimento: "))

idade = ano_curr - ano


if idade >= 18:
    print(f"Adulto - {idade}")
elif idade >= 12:
    print(f"Adolescente - {idade}")
else:
    print(f"criança - {idade}")




"""
faça um porgrama onde é pedido ao utlizador 3 numeros: num1, num2

se num1 > 20 - escreva na consola opt1
se num2 > 30 e num1 <= 20 - escreva na consola opt2
se nao imprima - opt3

deve usar o if, elif else
"""

num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))

if num1 > 20:
    print(f"opt1")
elif num2 > 30: # sei q num1 <= 20
    print(f"opt2")
else:
    print(f"opt3")

