#Criar
#idx        0         1      2       3       4
#pos        1         2      3       4       5
from itertools import count

from conda.notices.views import print_notices

nomes = ["João", "Carlos", "Ana", "Rita", "Joana"]

print(nomes)

#acder a um elem

print(nomes[0]) # nomes[idx], x -> idx do valor a ler

# print(nomes[9])

"""

Crie uma lista com 10 nomes de pessoas
mostre:
- a 1ª posição
- a 10ª posição
- a 4ª posição

"""
print("------")
nomes2 = [
    "João", "Carlos", "Ana", "Rita", "Joana",
          "Luis", "Diana", "Jose", "Pedro", "Nuno"
          ]
print(nomes2[0])
print(nomes2[9])
print(nomes2[3])
print("------")

# ver qts elm ha na lista

print(len(nomes2)) # devolve o número de elm da lista


"""

tem uma lista (lst) onde desconhece o numero de elementos que estão na lista
como mostrar o ultimo elemento?



lst[len(lst)-1]

len(lst) -> num de elementos
len(lst)-1 -> idx do ultimo elemento
"""
print("------")
print("------")
# add elem

notas = [10, 13, 13, 7, 9]

print(notas)
print(len(notas))
## add no fim
print("---add no fim---")

notas.append(18)
print(notas)
print(len(notas))


## add no inicio/meio


print("---add no inicio---")

notas.insert(0, 9)
#
# [10, 13, 13, 7, 9, 18]
# [  ,10, 13, 13, 7, 9, 18]
# [9 ,10, 13, 13, 7, 9, 18]
print(notas)
print(len(notas))


print("---add no uma lista no fim---")
## add no uma lista no fim


notas.insert(4, 19)

# [9,10, 13, 13, 19 ,7, 9, 18]

print(notas)
print(len(notas))



print("---modificar um valor na lista---")

# modificar um valor na lista
print(notas)
print(len(notas))

notas[0] = 19

print(notas)
print(len(notas))


print("----iterar pela lista ----")
notas[7] = 8
# iterar pela lista

def aprovado(nota):
    if nota >= 10:
        print("Aprovado")
    else:
        print("Reprovado")

print(notas)
for i in notas:
    print(f"valor do i:  {i}")
    aprovado(i)



"""

Faça um com uma lista de 5 números inteiros e mostre os 5 números 

"""



"""
Faça um Programa que leia um lista de 10 números inteiros  e mostre-os na ordem inversa.

"""
print("------")
print("------")

lista = []


for i in range(1, 11):
    num = int(input(f"digite o num {i}: "))
    lista.append(num)




for i in range(len(lista)):
    print(lista[ len(lista) - i - 1])