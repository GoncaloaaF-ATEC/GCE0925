"""

var
in/out

op com var


if
    if else
    if elif else


match-case



"""

# loops -> repetir codigo

# while

num = 10

while num > 0:
    print(num)
    num -= 1

"""

faça uma app que peça 1 num ao utilizador e mostre todos os valores de 0 ate esse num.
Exemplos::
num -> 3
out 0
    1
    2
    3 
----   
num -> 5
out 0
    1
    2
    3
    4
    5

"""

num = int(input('num: '))
aux = 0

while  aux <= num:
    print(aux, end=' ')
    aux += 1

print("")




"""

faça uma app que peça 2 números ao utilizador e mostre todos os valores entre esses dois números 
por ordem crescente.

use so um loop while
"""

num1=int(input("DIGITE O NUMERO: "))
num2=int(input("DIGITE O NUMERO: "))

if num2 < num1 :
    temp = num2
    num2 = num1
    num1 = temp

while num1 != num2 :
    num1 += 1
    print(num1)



"""

faça uma app que peça 2 números ao utilizador e mostre todos os valores entre esses dois números 
pregunte ao utilizador se quer ordenados ascendente ou descendente

use so um loop while
"""


# pedir num ao user

# preguntava se quer ordenados crescente ou descendente


# maior
# menor

if num2 > num1 :
    # num2 = num2 - num1
    # num1 = num1 + num2
    # num2 = num1 - num2
    max = num2
    min = num1

# se descendente
# inverto a ordem

#mostrar val

